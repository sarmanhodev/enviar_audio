from flask import *
from gtts import gTTS
import time
import os
import uuid
import requests

app = Flask(__name__)

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)



# ---------------------------------------------------------
# 🔊 Gera arquivo MP3 com nome único usando UUID
# ---------------------------------------------------------
def text_to_speech(text):
    # Sempre cria o nome antes
    filename = f"{uuid.uuid4().hex}.mp3"
    path = os.path.join(AUDIO_DIR, filename)

    try:
        # Sessão customizada
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 ...'
        })

        tts = gTTS(text=text, lang="pt", slow=False, session=session)
        tts.save(path)

    except Exception as e:
        # Fallback (sem session)
        try:
            tts = gTTS(text=text, lang="pt", slow=False)
            tts.save(path)

        except Exception as fallback_error:
            raise Exception(f"Erro: {e}. Fallback falhou: {fallback_error}")

    return path




@app.route("/home", methods=["GET", "POST"])
def home():
    audio_files = []
    if os.path.exists(AUDIO_DIR):
        audio_files = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.mp3')]

    return render_template("home.html", voices=[], audio_files=audio_files)


# ---------------------------------------------------------
# 🔥 POST: Converter texto → áudio
# ---------------------------------------------------------
@app.route("/getText", methods=["GET", "POST"])
def getText():
    if request.method == 'POST':
        try:
            dados = request.get_json()
            texto = dados[0].get('texto')

            if not texto:
                return jsonify({"status": 400, "message": "Texto não pode estar vazio."}), 400

            # Converte texto em áudio com nome exclusivo
            filename = text_to_speech(texto)

            # (Opcional) Limpeza automática
            # limpar_audios_antigos()

            return jsonify({
                "status": 200,
                "message": "Texto convertido com sucesso.",
                "audio_url": f"/{filename}",
                "filename": filename
            }), 200

        except Exception as e:
            print("Erro inesperado:", str(e))
            return jsonify({"status": 500, "message": "Erro interno do servidor."}), 500

    return jsonify({"status": 405, "message": "Método não permitido."}), 405


# ---------------------------------------------------------
# 🗑️ POST: Excluir áudio específico
# ---------------------------------------------------------
@app.route("/excluir_audio", methods=["POST"])
def excluir_audio():
    try:
        dados = request.get_json()
        filename = dados[0].get("filename")

        if not filename:
            return jsonify({"status": 400, "message": "Arquivo não informado."}), 400

        path = os.path.join(filename)

        if os.path.exists(path):
            os.remove(path)
            return jsonify({"status": 200, "message": "Áudio excluído com sucesso!"}), 200
        else:
            return jsonify({"status": 404, "message": "Arquivo não encontrado."}), 404

    except Exception as e:
        print("Erro inesperado:", str(e))
        return jsonify({"status": 500, "message": "Erro interno do servidor."}), 500
    

# ---------------------------------------------------------
# 🎵 Rota pública para servir áudios
# ---------------------------------------------------------
@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)


if __name__ == "__main__":
    app.run(debug=True)



