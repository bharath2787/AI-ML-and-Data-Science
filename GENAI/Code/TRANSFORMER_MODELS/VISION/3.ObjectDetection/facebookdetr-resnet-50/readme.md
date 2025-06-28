

````markdown
#  Object Detection with DETR (facebook/detr-resnet-50)

This project demonstrates how to perform end-to-end object detection using [Facebook's DETR (DEtection TRansformer)](https://huggingface.co/facebook/detr-resnet-50) model. The app uses the `facebook/detr-resnet-50` checkpoint from Hugging Face Transformers to detect objects in images without requiring any hand-crafted region proposal stages.

---

##  Features

- Transformer-based object detection (DETR)
- Pretrained on COCO dataset (91 object classes)
- Simple Gradio interface for interactive image uploads
- Real-time bounding box visualization with confidence scores

---

##  Demo

Upload any image, and the model will return the same image with detected objects highlighted by bounding boxes and labels.

---

##  Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
````

### `requirements.txt`

```txt
torch
transformers
Pillow
gradio
```

---

##  Run the App

```bash
python app.py
```

The app will launch in your browser at `http://localhost:7860`.

---

##  Model Details

* **Model:** `facebook/detr-resnet-50`
* **Type:** End-to-end object detector
* **Architecture:** ResNet-50 backbone + Transformer encoder-decoder
* **Dataset:** COCO 2017 (91 classes)

> This model predicts bounding boxes and class labels directly using transformers, eliminating the need for post-processing steps like non-max suppression.

---

##  References

* [DETR paper (Facebook AI)](https://arxiv.org/abs/2005.12872)
* [Hugging Face Model Card](https://huggingface.co/facebook/detr-resnet-50)
* [Transformers Documentation](https://huggingface.co/docs/transformers)

---
