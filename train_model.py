from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset

def load_and_process_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        texts = f.readlines()
    return {"text": texts}

def train_model(train_file):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token

    dataset = load_and_process_data(train_file)
    dataset = Dataset.from_dict(dataset)
    tokenized_dataset = dataset.map(lambda e: tokenizer(e['text'], truncation=True, padding='max_length', max_length=128), batched=True)

    model = GPT2LMHeadModel.from_pretrained('gpt2')

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    training_args = TrainingArguments(
        output_dir="./results",
        overwrite_output_dir=True,
        num_train_epochs=1,
        per_device_train_batch_size=2,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset,
    )

    trainer.train()

if __name__ == "__main__":
    train_file = "training_data.txt"
    train_model(train_file)
