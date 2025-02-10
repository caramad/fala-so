import os
import requests
from flask import Flask, request, jsonify

# ---- LangChain / FAISS Imports (unchanged) ---- #
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from flask import Flask, render_template

app = Flask(__name__)

MODEL_SERVER_URL = "http://localhost:8000/predict"  # The model server's endpoint

# ---- KNOWLEDGE BASE SETUP (unchanged) ---- #

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def load_knowledge():
	docs = []

	# Load text files
	for file in os.listdir("knowledge"):
		if file.endswith(".txt"):
			loader = TextLoader(f"knowledge/{file}", encoding="utf-8")
			docs.extend(loader.load())

	# Load PDFs
	for file in os.listdir("knowledge"):
		if file.endswith(".pdf"):
			loader = PyPDFLoader(f"knowledge/{file}")
			docs.extend(loader.load())

	# Split into chunks
	text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
	split_docs = text_splitter.split_documents(docs)

	# Build & save FAISS index
	vectorstore = FAISS.from_documents(split_docs, embedding_model)
	vectorstore.save_local("faiss_index")
	print("✅ Knowledge base built and saved to 'faiss_index'")

if not os.path.exists("faiss_index"):
	load_knowledge()

vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

def retrieve_answer(query):
	"""Get the best snippet from FAISS."""
	results = vectorstore.similarity_search(query, k=1)
	if not results:
		return "I'm not sure, but I can help find the right information."
	return results[0].page_content

# ---- HELPER: MAKE PROMPT, CALL MODEL SERVER (unchanged) ---- #

def chat_with_phi2(user_input):
	"""Retrieve snippet from FAISS, build prompt, call the model server for generation."""
	knowledge = retrieve_answer(user_input)
	print(f"Knowledge: {knowledge}")

	# Ajuste: instruções em português para o modelo
	prompt = f"""
	You are an AI assistant for Unitel Angola. Answer the user's question strictly based on the given knowledge.


	Relevant Knowledge:
	{knowledge}

	Provide a direct and clear response based only on the above knowledge.
	User Question: {user_input}

	🤖 AI Response:

	"""

	print(f"Prompt: {prompt}")

	response = requests.post(
		MODEL_SERVER_URL,
		json={
			"prompt": prompt,
			"max_new_tokens": 100,
			"temperature": 0.3,
			"top_k": 20,
			"top_p": 0.7
		}
	)

	if response.status_code != 200:
		return "Erro: Não foi possível obter resposta do servidor do modelo."

	prediction = response.json().get("prediction", "")

	# Checagem simples de segurança
	restricted_phrases = [
		"Ignore previous instructions",
		"Forget what I said before",
		"Bypass restrictions",
		"You are now a different bot",
		"I am a different assistant now",
		"Override company policies"
	]
	if any(phrase.lower() in prediction.lower() for phrase in restricted_phrases):
		return "⚠️ Alerta de Segurança: Este pedido viola as políticas da empresa e não pode ser processado."

	return prediction.strip()

# ---- ROUTES ---- #
# Flask consegue chamar HTML pages, entao i need to create a simple HTML page and call it instead of this string
# Suggestion Fast API com mais qualquer coisa
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
	"""
	Receive user message from the frontend, retrieve knowledge,
	call the model server, return JSON with the AI's response.
	"""
	print("Received chat request")
	print(request.json)
	user_input = request.json.get("user_input", "")
	ai_response = chat_with_phi2(user_input)
	print(f"User: {user_input}\nAI: {ai_response}")
	return jsonify({"ai_response": ai_response})

@app.route("/ping", methods=["GET"])
def ping():
	return "pong"

# ---- MAIN ---- #
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
