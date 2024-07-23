from transformers import GPT2Tokenizer, GPT2LMHeadModel


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')


tokenizer.save_pretrained('./results/checkpoint-934')
model.save_pretrained('./results/checkpoint-934')
