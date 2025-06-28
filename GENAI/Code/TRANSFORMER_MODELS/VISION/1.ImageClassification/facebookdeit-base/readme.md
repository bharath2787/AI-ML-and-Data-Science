
````markdown
# DeiT Base Patch16 Image Classification App

This is a simple image classification web app using Facebook's **DeiT-base-patch16-224** model via Hugging Face Transformers.

---

## Features

- Classifies images into 1000 ImageNet classes
- Uses the DeiT (Data-efficient Image Transformer) architecture
- Powered by PyTorch and Hugging Face Transformers
- Simple Gradio web UI for uploading images and viewing predictions
- Automatically uses GPU if available

---

## Installation

1. Clone this repository or download the code.

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
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

This will start a local web server and open a browser interface where you can upload images and get classification results.

---

## Files

* `app.py` — Main script running the classifier and UI
* `requirements.txt` — Dependencies list
* `README.md` — This file

---

## Model Details

* Model: `facebook/deit-base-patch16-224`
* Architecture: Data-efficient Image Transformer (DeiT) Base with 16x16 patches
* Dataset: ImageNet-1k (1000 classes)
* Source: [Hugging Face Model Hub](https://huggingface.co/facebook/deit-base-patch16-224)

---

## License

Open source under MIT License.

---

## Acknowledgments

* [Facebook Research DeiT](https://arxiv.org/abs/2012.12877)
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* [PyTorch](https://pytorch.org/)
* [Gradio](https://gradio.app/)

