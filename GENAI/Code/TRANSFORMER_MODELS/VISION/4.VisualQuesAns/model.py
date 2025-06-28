# Import necessary libraries
from transformers import BlipProcessor, BlipForQuestionAnswering  # For preprocessing and model loading
from PIL import Image  # For image handling
import torch  # For tensor operations and GPU/CPU handling

class BLIPVQAModel:
    """
    A class that wraps the BLIP Visual Question Answering model.
    Given an image and a question about the image, it returns an answer.
    """

    def __init__(self, device=None):
        """
        Initialize the processor and model.

        Args:
            device (str, optional): Specify 'cuda' for GPU or 'cpu'. If None, auto-selects based on availability.
        """
        # Automatically use GPU if available, else fall back to CPU
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        
        # Load the BLIP processor for preparing image + question input
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
        
        # Load the pre-trained BLIP VQA model and move it to the selected device
        self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base").to(self.device)

    def predict(self, image: Image.Image, question: str) -> str:
        """
        Generates an answer for a given image-question pair.

        Args:
            image (PIL.Image): The input image.
            question (str): The question to be asked about the image.

        Returns:
            str: The model's answer to the question.
        """
        # Preprocess the image and question into tensors, and move to the correct device
        inputs = self.processor(image, question, return_tensors="pt").to(self.device)

        # Generate the answer using the model (no need for gradients here)
        out = self.model.generate(**inputs)

        # Decode the output token IDs into a readable answer string
        return self.processor.decode(out[0], skip_special_tokens=True)



# BLIP (Bootstrapped Language Image Pretraining)	A model designed for tasks involving both vision and language (e.g., captioning, VQA).
# Processor	Handles converting raw inputs (image + text) into model-ready tensors.
# .generate()	Used to produce a text answer from the model, similar to how chat models generate replies.
# .decode()	Converts the output token IDs into human-readable text.
# skip_special_tokens=True	Removes special tokens like <s> or </s> from the generated answer.