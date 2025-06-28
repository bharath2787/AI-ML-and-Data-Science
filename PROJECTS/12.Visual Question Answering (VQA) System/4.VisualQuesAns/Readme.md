

````markdown
#  BLIP Visual Question Answering (VQA)

This project uses the [BLIP](https://huggingface.co/Salesforce/blip-vqa-base) model to perform Visual Question Answering (VQA). You can ask questions about an image and receive answers either via a **command-line interface** or a **Gradio web UI**.

---

##  Features

- 🔍 Ask questions about any image using the powerful BLIP model
- 💻 Run from the command line with ease
- 🌐 Interactive UI using Gradio
- 🛠️ Simple to set up and use

---

##  Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/blip_vqa_project.git
cd blip_vqa_project
````

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

##  Running the Project

###  CLI (Command-Line Interface)

```bash
python cli.py <image_path_or_url> "<your_question_here>"
```

**Example:**

```bash
python cli.py "https://example.com/cat.jpg" "What animal is this?"
```

###  Gradio Web App

```bash
python app.py
```

This will launch a local web interface in your browser where you can upload an image and ask a question.

---

## 🧠 Model Used

This project uses the [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base) model from Hugging Face.

> **Note:** The model typically returns concise answers (often one word) due to the nature of the VQA dataset it was trained on. For more descriptive responses, consider using models like **BLIP-2**, **LLaVA**, or **MiniGPT-4**.

---

## 📁 Project Structure

```
blip_vqa_project/
├── app.py              # Gradio interface
├── cli.py              # Command-line interface
├── model.py            # BLIP model wrapper
├── utils.py            # Utility functions (image loading)
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
```

---

## 📝 Example Questions

* "What color is the car?"
* "How many people are in the image?"
* "Is the animal sleeping?"
* "What is the man holding?"

---
