from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import requests
import torch
import gradio as gr

# Load model and processor
model_name = "google/vit-base-patch16-224"
model = ViTForImageClassification.from_pretrained(model_name)
processor = ViTImageProcessor.from_pretrained(model_name)
model.eval()  # set model to eval mode

# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Prediction function
def classify_image(image):
    # Preprocess image
    inputs = processor(images=image, return_tensors="pt").to(device)
    
    # Forward pass
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get predicted class index
    logits = outputs.logits
    predicted_idx = logits.argmax(-1).item()
    
    # Get label from model config
    predicted_label = model.config.id2label[predicted_idx]
    
    return predicted_label

# Build Gradio Interface
app = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="ViT-B/16 Image Classification",
    description="Upload an image and the ViT model will classify it."
)

# Launch app
app.launch()
