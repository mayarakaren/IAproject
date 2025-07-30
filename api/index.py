# Importando bibliotecas principais
from flask import Flask, request, jsonify, url_for, send_from_directory # Flask para API web
from flask_cors import CORS                         # Para permitir que o front acesse a API
from deepface import DeepFace                       # DeepFace para detectar emoções faciais
import random                                       # Para escolher imagem aleatória
import os                                           # Para acessar arquivos e pastas
import cv2                                          # OpenCV para ler a imagem
import numpy as np                                  # Para converter bytes em imagem

# Inicializando o app Flask
app = Flask(__name__, static_folder="../frontend/static", static_url_path="")
CORS(app)

# Mapeia emoções para as pastas de imagens
emocoes_para_pastas = {
    "happy": "static/mar_feliz",
    "sad": "static/mar_triste",
    "neutral": "static/mar_neutro"
}

# Função auxiliar para escolher uma imagem aleatória de uma pasta
def escolher_imagem(emocao):
    pasta = emocoes_para_pastas.get(emocao, "static/mar_neutro")
    # Verifica se a pasta realmente existe
    if not os.path.exists(pasta):
        print(f"Pasta não encontrada: {pasta}")
        return None
    
    arquivos = os.listdir(pasta)
    if arquivos:
        nome_arquivo = random.choice(arquivos)
        return os.path.join(pasta, nome_arquivo).replace("\\", "/")  # garante compatibilidade no Windows
    return None

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def frontend_arquivos(filename):
    return send_from_directory("../frontend", filename)

# Rota principal da API que analisa a emoção de uma imagem enviada
@app.route("/analisa-rosto", methods=["POST"])
def analisa_rosto():
    # Verifica se a imagem foi enviada no corpo da requisição
    if 'imagem' not in request.files:
        return jsonify({"erro": "Nenhuma imagem enviada"}), 400

    imagem_file = request.files['imagem']

    # Converte a imagem enviada para um array NumPy (formato do OpenCV)
    npimg = np.frombuffer(imagem_file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    try:
        # Analisa a emoção com DeepFace
        resultado = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emocao = resultado[0]['dominant_emotion']
        print(f"Emoção detectada: {emocao}")

        # Seleciona uma imagem de fundo com base na emoção
        imagem_fundo = escolher_imagem(emocao)
        print("Imagem fundo escolhida:", imagem_fundo)


        # Se encontrar uma imagem, retorna a resposta
        if imagem_fundo:
            relativo = imagem_fundo.split("static/")[-1].replace("\\", "/")
            print("Caminho relativo:", relativo)
            imagem_url = url_for('static', filename=relativo)
            print("URL final:", imagem_url)
            return jsonify({
                "emocao": emocao,
                "imagem_fundo": imagem_url  # URL completa acessível pelo front
            })
        # Caso não encontre nenhuma imagem
        return jsonify({"erro": "Imagem não encontrada"}), 404

    # Se acontecer algum erro durante a análise
    except Exception as e:
        print("ERRO:", str(e))
        return jsonify({"erro": str(e)}), 500

# Inicia o servidor local do Flask
if __name__ == "__main__":
    app.run(debug=True)

app = app