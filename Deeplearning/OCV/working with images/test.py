from pathlib import Path
import shutil

# Create a directory for the notebook and assets
notebook_dir = Path("/mnt/data/Face_Detection_OpenCV")
notebook_dir.mkdir(parents=True, exist_ok=True)

# Sample image placeholder (user should replace with actual image)
sample_image_path = notebook_dir / "face_sample.jpg"
with open(sample_image_path, "wb") as f:
    f.write(b"")  # Empty placeholder

# Prepare notebook content as .ipynb structure
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Face Detection with OpenCV - Haar Cascade Classifier\n",
    "\n",
    "In this notebook, we'll demonstrate how to perform face detection using OpenCV's `CascadeClassifier`.  \n",
    "We'll detect faces in images, draw bounding boxes, and save cropped face regions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is Haar Cascade?\n",
    "- Haar cascades are pre-trained classifiers based on Haar features.\n",
    "- OpenCV provides XML files trained to detect faces, eyes, smiles, etc.\n",
    "- These classifiers work by scanning images at multiple scales and locations.\n",
    "\n",
    "We'll use:  \n",
    "`haarcascade_frontalface_default.xml` – trained for detecting frontal human faces."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "import os\n",
    "\n",
    "def show_img(img, title=\"Image\"):\n",
    "    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
    "    plt.figure(figsize=(6, 4))\n",
    "    plt.imshow(img_rgb)\n",
    "    plt.title(title)\n",
    "    plt.axis(\"off\")\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Load Haar Cascade Classifier\n",
    "`CascadeClassifier()` is a class in OpenCV used to load the cascade XML file.\n",
    "\n",
    "**Syntax:**  \n",
    "```python\n",
    "cv2.CascadeClassifier(path_to_xml)\n",
    "```\n",
    "\n",
    "You must check if the classifier loaded correctly using `.empty()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n",
    "if face_cascade.empty():\n",
    "    print(\"Error: Haar cascade XML not loaded!\")\n",
    "else:\n",
    "    print(\"Haar cascade loaded successfully.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = cv2.imread(\"face_sample.jpg\")\n",
    "if img is None:\n",
    "    raise FileNotFoundError(\"Image not found. Please ensure 'face_sample.jpg' exists in the current directory.\")\n",
    "\n",
    "gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "show_img(img, \"Original Image\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Why convert to grayscale?\n",
    "Haar cascades work on single-channel images (grayscale), not color images."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "faces = face_cascade.detectMultiScale(\n",
    "    gray,\n",
    "    scaleFactor=1.1,\n",
    "    minNeighbors=5,\n",
    "    minSize=(30, 30)\n",
    ")\n",
    "print(f\"Detected {len(faces)} face(s).\")\n",
    "\n",
    "for (x, y, w, h) in faces:\n",
    "    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)\n",
    "\n",
    "show_img(img, \"Detected Faces\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### detectMultiScale()\n",
    "**Parameters:**\n",
    "- `scaleFactor`: Image size reduction per scale\n",
    "- `minNeighbors`: Number of rectangles that must be grouped\n",
    "- `minSize`: Minimum face size to detect\n",
    "\n",
    "**Returns:** List of bounding boxes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.exists(\"cropped_faces\"):\n",
    "    os.makedirs(\"cropped_faces\")\n",
    "\n",
    "img_original = cv2.imread(\"face_sample.jpg\")\n",
    "\n",
    "for idx, (x, y, w, h) in enumerate(faces):\n",
    "    face_crop = img_original[y:y+h, x:x+w]\n",
    "    path = f\"cropped_faces/face_{idx+1}.jpg\"\n",
    "    cv2.imwrite(path, face_crop)\n",
    "    print(f\"Saved: {path}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

# Save notebook file
notebook_path =  "04_Face_Detection_with_OpenCV.ipynb"
import json
with open(notebook_path, "w") as f:
    json.dump(notebook_content, f)

# notebook_path.name  # Return the file name only

