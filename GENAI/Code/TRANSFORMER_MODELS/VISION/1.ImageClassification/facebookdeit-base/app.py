# Import necessary libraries
from transformers import ViTForImageClassification, ViTImageProcessor  # For loading the ViT model and preprocessor
from PIL import Image  # To handle image input
import torch  # For tensor operations and GPU support
import gradio as gr  # For creating a simple web UI

# -----------------------------
# STEP 1: Load the Pre-trained Model
# -----------------------------

# Name of the pretrained model from Hugging Face model hub
model_name = "facebook/deit-base-patch16-224"

# Load the Vision Transformer (ViT) model for image classification
model = ViTForImageClassification.from_pretrained(model_name)

# Load the corresponding image processor to preprocess inputs for the model
processor = ViTImageProcessor.from_pretrained(model_name)

# Set the model to evaluation mode (disables training-specific operations like dropout)
model.eval()

# -----------------------------
# STEP 2: Move Model to GPU (if available)
# -----------------------------

# Check if a GPU (CUDA) is available and use it if possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Move the model to the selected device (GPU or CPU)
model.to(device)

# -----------------------------
# STEP 3: Define the Prediction Function
# -----------------------------

def classify_image(image):
    """
    This function receives an image and returns the predicted label.
    """
    # Preprocess the image: resize, normalize, and convert to tensor
    inputs = processor(images=image, return_tensors="pt").to(device)

    # Perform forward pass through the model (no gradient needed)
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract raw output scores (logits)
    logits = outputs.logits

    # Find the index of the class with the highest score
    predicted_class_idx = logits.argmax(-1).item()

    # Convert the index to the actual class label using the model's config
    predicted_label = model.config.id2label[predicted_class_idx]

    return predicted_label

# -----------------------------
# STEP 4: Create a Gradio Web Interface
# -----------------------------

# Create a simple UI using Gradio
app = gr.Interface(
    fn=classify_image,  # The function to call when an image is uploaded
    inputs=gr.Image(type="pil"),  # Input type: Image (as a PIL object)
    outputs="text",  # Output type: Text (label of predicted class)
    title="DeiT Base Patch16 Image Classifier (ViT)",  # Title of the web app
    description="Upload an image to classify it using the ViT-based facebook/deit-base-patch16-224 model."  # Description shown in the UI
)

# Launch the Gradio app in a local server (a public link will also be provided)
app.launch()
