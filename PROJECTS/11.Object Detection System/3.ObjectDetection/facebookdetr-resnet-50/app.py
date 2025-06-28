# Import necessary libraries
import torch  # For model inference and GPU/CPU handling
from transformers import DetrImageProcessor, DetrForObjectDetection  # DETR model and preprocessor
from PIL import Image, ImageDraw, ImageFont  # For image processing and annotation
import requests  # (Optional, used to download images)
import gradio as gr  # For creating a simple web interface

# -----------------------------------------------
# STEP 1: Load the Pre-trained DETR Model
# -----------------------------------------------

# Define the model name from Hugging Face model hub
model_name = "facebook/detr-resnet-50"

# Load the processor which handles image preprocessing and post-processing
processor = DetrImageProcessor.from_pretrained(model_name)

# Load the DETR model for object detection
model = DetrForObjectDetection.from_pretrained(model_name)
model.eval()  # Set the model to evaluation mode (disables training-specific layers)

# Move the model to GPU if available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# -----------------------------------------------
# STEP 2: Helper Function to Draw Bounding Boxes
# -----------------------------------------------

def draw_boxes(image, outputs, threshold=0.7):
    """
    Draws bounding boxes and labels on the image for all detected objects 
    with confidence above the given threshold.
    
    Args:
        image (PIL.Image): The original input image.
        outputs (dict): Detection outputs with 'scores', 'labels', and 'boxes'.
        threshold (float): Minimum score to display a detection.
        
    Returns:
        image (PIL.Image): The image with bounding boxes and labels drawn.
    """
    draw = ImageDraw.Draw(image)

    # Load a font for drawing labels; fallback to default if not found
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()

    # Loop through each detected object
    for score, label, box in zip(outputs['scores'], outputs['labels'], outputs['boxes']):
        if score > threshold:
            box = box.tolist()  # Convert tensor to list
            x0, y0, x1, y1 = box  # Coordinates of the bounding box

            # Draw a red rectangle around the detected object
            draw.rectangle(box, outline="red", width=3)

            # Get the human-readable label using the model's label map
            label_text = f"{model.config.id2label[label.item()]}: {score:.2f}"

            # Get the size of the text box to avoid overlapping
            text_bbox = draw.textbbox((x0, y0), label_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            # Adjust label position so it doesn't go off the top of the image
            text_y = y0 - text_height if y0 - text_height > 0 else y0

            # Draw background for the label
            draw.rectangle([x0, text_y, x0 + text_width, text_y + text_height], fill="red")

            # Draw the label text
            draw.text((x0, text_y), label_text, fill="white", font=font)

    return image

# -----------------------------------------------
# STEP 3: Object Detection Pipeline Function
# -----------------------------------------------

def detect_objects(image):
    """
    Performs object detection on the given image and returns the annotated image.
    
    Args:
        image (PIL.Image): The uploaded image.
        
    Returns:
        image (PIL.Image): Annotated image with detected objects.
    """
    # Preprocess image and move inputs to device
    inputs = processor(images=image, return_tensors="pt").to(device)

    # Run the model in inference mode (no gradient computation)
    with torch.no_grad():
        outputs = model(**inputs)

    # Prepare original image size in the format (height, width)
    target_sizes = [torch.tensor([image.height, image.width])]

    # Convert raw model output to bounding boxes, scores, and labels
    results = processor.post_process_object_detection(
        outputs,
        threshold=0.7,
        target_sizes=target_sizes
    )[0]

    # Draw bounding boxes on a copy of the image and return it
    return draw_boxes(image.copy(), results)

# -----------------------------------------------
# STEP 4: Create Gradio Web Interface
# -----------------------------------------------

# Set up a simple UI using Gradio
app = gr.Interface(
    fn=detect_objects,  # Function to run when an image is uploaded
    inputs=gr.Image(type="pil"),  # Input type: Image (as PIL)
    outputs="image",  # Output: Annotated image with boxes
    title="Object Detection with DETR (ResNet-50)",  # Web app title
    description="Upload an image and this app will detect objects using Facebook's DETR ResNet-50."  # Short description
)

# -----------------------------------------------
# STEP 5: Launch the Web App
# -----------------------------------------------

app.launch()  # Start the app locally and provide a shareable link
