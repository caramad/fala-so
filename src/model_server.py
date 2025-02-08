import torch
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

# Choose your model
MODEL_NAME = "microsoft/phi-2"
device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading tokenizer & model. This may take a while...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
	"""Receive a prompt, generate text, return the result as JSON."""
	data = request.json
	if not data or "prompt" not in data:
		return jsonify({"error": "No prompt provided"}), 400

	prompt = data["prompt"]
	max_new_tokens = data.get("max_new_tokens", 100)
	temperature = data.get("temperature", 0.3)
	top_k = data.get("top_k", 30)
	top_p = data.get("top_p", 0.7)

	# Tokenize prompt
	inputs = tokenizer(prompt, return_tensors="pt").to(device)
	num_tokens = inputs["input_ids"].shape[1]

	output = model.generate(
			**inputs,
			max_new_tokens=max_new_tokens,
			temperature=temperature,
			top_k=top_k,
			top_p=top_p,
			pad_token_id=tokenizer.eos_token_id,
			do_sample=True,
			eos_token_id=tokenizer.eos_token_id,  # Ensure the model knows where to stop
			stopping_criteria=None  # Allow the model to finish naturally
		)

	generated_tokens = output[0][num_tokens:]
	prediction = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

	return jsonify({"prediction": prediction})

if __name__ == "__main__":
	# Run on a separate port, e.g. 8000
	app.run(host="0.0.0.0", port=8000, debug=False)
