import sys
from transformers import pipeline

def main(long_text, prompt):
    # Load the BART model suitable for text summarization
    model = pipeline("summarization", model="facebook/bart-large-cnn")

    # Generate output based on the long text and the prompt
    output = model(long_text, max_length=50, min_length=25, do_sample=False)  # Adjust lengths as needed

    # Print the generated output
    print("Generated Output:")
    print(output[0]['summary_text'])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python text_generator.py '<long_text>' '<prompt>'")
        sys.exit(1)

    long_text = sys.argv[1]
    prompt = sys.argv[2]  # This can be kept for reference, but won't be used in generation

    main(long_text, prompt)
