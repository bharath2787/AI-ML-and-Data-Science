#  Image-to-Text Captioning with BLIP

This project demonstrates an **image captioning solution** powered by [Hugging Face Transformers](https://huggingface.co/docs/transformers/) using the **BLIP (Bootstrapped Language Image Pretraining)** model. It includes:

-  A command-line interface (CLI) for captioning images
-  A beautiful Gradio web app for interactive use

---

##  Features

- Generate natural language captions for any image
- Powered by `Salesforce/blip-image-captioning-base`
- Two modes of use: CLI and Web UI
- Lightweight and runs in a Python virtual environment

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/image2text.git
cd image2text

python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux

pip install --upgrade pip
pip install -r requirements.txt

python cli.py path/to/your/image.jpg

#to run app
python app.py