import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image: Image.Image) -> str:
    image = image.convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# ✨ UI layout
with gr.Blocks(css="""
#title {text-align: center; font-size: 2.2rem; font-weight: bold; padding-bottom: 0.5rem;}
#desc {text-align: center; font-size: 1.1rem; color: gray;}
#output {font-size: 1.2rem;}
""") as demo:
    gr.Markdown("<div id='title'>🧠 Image Captioning with BLIP</div>")
    gr.Markdown("<div id='desc'>Upload an image and get a human-like caption using Hugging Face's BLIP model.</div>")

    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            image_input = gr.Image(type="pil", label="Upload Image")
            caption_output = gr.Textbox(label="Generated Caption", lines=2, interactive=False, elem_id="output")
            download_btn = gr.Button("Download Caption")
        with gr.Column(scale=1):
            gr.Examples(
                examples=[
                    "examples/cat.jpg",
                    "examples/street.jpg",
                ],
                inputs=image_input,
                label="Example Images"
            )

    image_input.change(fn=generate_caption, inputs=image_input, outputs=caption_output)
    
    def download_caption(caption):
        with open("caption.txt", "w", encoding="utf-8") as f:
            f.write(caption)
        return "caption.txt"

    download_btn.click(download_caption, inputs=caption_output, outputs=gr.File(label="Download Your Caption"))

demo.launch()
