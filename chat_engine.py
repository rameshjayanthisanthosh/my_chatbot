from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("openchat/openchat_3.5")
model = AutoModelForCausalLM.from_pretrained("openchat/openchat_3.5", torch_dtype=torch.float32)

def get_response(user_input):
    prompt = f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("<|assistant|>")[-1].strip()
