# Import necessary libraries
from PIL import Image  # For loading and processing images
import requests  # To fetch images from URLs over the internet
from io import BytesIO  # To handle image bytes in memory

def load_image(image_path_or_url):
    """
    Loads an image from a local path or a URL.
    
    Args:
        image_path_or_url (str): The file path or URL of the image.
        
    Returns:
        PIL.Image: The loaded image in RGB format.
    """
    
    # Check if the input is a URL (starts with http or https)
    if image_path_or_url.startswith("http://") or image_path_or_url.startswith("https://"):
        # Send an HTTP GET request to fetch the image
        response = requests.get(image_path_or_url)
        
        # Convert the downloaded bytes into an image object
        return Image.open(BytesIO(response.content)).convert("RGB")
    
    # If not a URL, treat the input as a local file path and open the image
    return Image.open(image_path_or_url).convert("RGB")
