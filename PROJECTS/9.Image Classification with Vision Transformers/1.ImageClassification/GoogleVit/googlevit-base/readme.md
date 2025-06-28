````markdown
# ViT-B/16 Image Classification App

This is a simple web app for image classification using the **Vision Transformer (ViT)** model `google/vit-base-patch16-224` from Hugging Face.

---

## Features

- Classifies input images into 1000 ImageNet categories
- Uses Hugging Face Transformers and PyTorch
- Easy-to-use Gradio web interface for uploading images and viewing predictions
- Runs on CPU or GPU automatically

---

## Installation

1. Clone this repository or download the code.

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the app:

```bash
python app.py
```

This will launch a local web server and open the Gradio interface in your browser. Upload an image and get the predicted label.

---

## Files

* `app.py` — Main script running the classification model and Gradio UI
* `requirements.txt` — Python dependencies

---

## Model Details

* Model: `google/vit-base-patch16-224`
* Architecture: Vision Transformer (ViT) Base with 16x16 patch size
* Dataset: ImageNet-1k (1000 classes)
* Source: [Hugging Face Model Hub](https://huggingface.co/google/vit-base-patch16-224)

---



## Acknowledgments

* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* [PyTorch](https://pytorch.org/)
* [Gradio](https://gradio.app/)
* [Google Research Vision Transformer](https://arxiv.org/abs/2010.11929)

