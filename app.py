from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure o Google Gemini (substitua pela sua chave real)
google_api_key = "AIzaSyD4C3ygccT8UUFa6nowbbeFBdYa-7jzguU" 
genai.configure(api_key=google_api_key)
generation_config = { "candidate_count": 1, "temperature": 0.5 }
safety_settings = { 'HATE': 'BLOCK_NONE', 'HARASSMENT': 'BLOCK_NONE', 'SEXUAL': 'BLOCK_NONE', 'DANGEROUS': 'BLOCK_NONE'}
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
chat = model.start_chat(history=[])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/processar", methods=["POST"])
def processar():
    data = request.get_json()
    custo_total = float(data.get('custo_total'))
    quanto_gastar = float(data.get('gastar'))
    tempo_meta = int(data.get('tempo_meta'))
    tempo2_meta = data.get('tempo2_meta')
    moeda = data.get('moeda')
    moeda2 = data.get('moeda2')
    sonho = data.get('sonho')

    if sonho:
        prompt = f"{sonho}, que custa no total {moeda} {custo_total:.2f}, mas consigo gastar apenas {moeda2} {quanto_gastar:.2f}, e tenho um periodo de {tempo_meta} {tempo2_meta}."
        response = chat.send_message(prompt)
        return jsonify({"resposta": response.text})
        return jsonify({"______________________"})
    else:
        return jsonify({"error": "Por favor, descreva seu sonho."})

if __name__ == "__main__":
    app.run(debug=True)