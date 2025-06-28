# text_summarization.py

import sys
from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments
from datasets import load_dataset

def main():
    # Load the tokenizer and model
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Load the dataset (e.g., CNN/Daily Mail)
    dataset = load_dataset("cnn_dailymail", "3.0.0")

    # Prepare the training and validation datasets
    train_dataset = dataset['train'].select(range(1000))  # Selecting first 1000 samples for training
    val_dataset = dataset['validation'].select(range(200))  # Selecting first 200 samples for validation

    # Tokenization function
    def preprocess_function(examples):
        model_inputs = tokenizer(
            examples["article"],
            max_length=1024,  # Max length for input text
            truncation=True,
        )
        with tokenizer.as_target_tokenizer():
            labels = tokenizer(
                examples["highlights"],
                max_length=128,  # Max length for summary
                truncation=True,
            )

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)
    tokenized_val_dataset = val_dataset.map(preprocess_function, batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",  # Change to 'steps' if needed
        eval_strategy="epoch",  # Update to new naming convention
        learning_rate=2e-5,
        per_device_train_batch_size=2,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        save_total_limit=2,  # Limit the total amount of checkpoints
    )

    # Create the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_val_dataset,  # Add validation dataset here
    )

    # Fine-tune the model
    trainer.train()

    # Save the model
    trainer.save_model("summarization_model")

    # Example text to summarize
    text = """Your long input text here. This should be a detailed paragraph that you want to summarize."""
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=130, min_length=30, do_sample=False)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("Summary:", summary)

if __name__ == "__main__":
    main()
