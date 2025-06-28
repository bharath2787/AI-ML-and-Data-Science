import argparse
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

def main():
    parser = argparse.ArgumentParser(description="Generate caption for an image using BLIP.")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()

    # Load processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load and preprocess image
    image = Image.open(args.image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # Generate caption
    with torch.no_grad():
        out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    print("Caption:", caption)

if __name__ == "__main__":
    main()
