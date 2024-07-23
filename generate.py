from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "results/checkpoint-934"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))

input_text = "Introduceți textul aici"
print(f"Input text: {input_text}")

inputs = tokenizer.encode(input_text, return_tensors='pt')
print(f"Tokenized inputs: {inputs}")


attention_mask = torch.ones(inputs.shape, dtype=torch.long)
print(f"Attention mask: {attention_mask}")


pad_token_id = tokenizer.pad_token_id

output = model.generate(
    inputs,
    attention_mask=attention_mask,
    max_length=50,
    num_return_sequences=1,
    pad_token_id=pad_token_id,
    no_repeat_ngram_size=2,  
    top_k=50,                
    top_p=0.95,             
    temperature=0.7,        
    do_sample=True,          
    num_beams=5,            
    early_stopping=True
)
print(f"Generated output tokens: {output}")

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(f"Generated text: {generated_text}")
