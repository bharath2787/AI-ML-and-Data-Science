import argparse
from model import BLIPVQAModel
from utils import load_image

def main():
    parser = argparse.ArgumentParser(description="BLIP VQA CLI")
    parser.add_argument("image", help="Path or URL to the image")
    parser.add_argument("question", help="Question to ask about the image")
    args = parser.parse_args()

    model = BLIPVQAModel()
    image = load_image(args.image)
    answer = model.predict(image, args.question)

    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
