from flask import *
from gtts import gTTS
import time
import os
import uuid
import requests
from conexao_supabase import *

app = Flask(__name__)

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


# ---------------------------------------------------------
# 🔊 Gera arquivo MP3 com nome único usando UUID
# ---------------------------------------------------------
def text_to_speech(text):
        # Pasta temporária para gerar áudio localmente antes do upload
        TMP_AUDIO_DIR = "tmp_audio"
        os.makedirs(TMP_AUDIO_DIR, exist_ok=True)

        # Gera nome único para o arquivo
        filename = f"{uuid.uuid4().hex}.mp3"
        tmp_path  = os.path.join(TMP_AUDIO_DIR, filename)


        tts = gTTS(text=text, lang="pt", tld="com", slow=False)
        tts.save(tmp_path)

        try:
           public_url = upload_audio(tmp_path, filename)
        except Exception as e:
            raise Exception(f"Erro ao enviar para Supabase: {str(e)}")
        finally:
            # Limpar arquivo local temporário
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

        # -------------------------------
        # 3️⃣ Retornar link público
        # -------------------------------
        public_url = supabase.storage.from_('audios').get_public_url(filename)
        return public_url



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


            return jsonify({
                "status": 200,
                "message": "Texto convertido com sucesso.",
                "texto_original": texto,
                "audio_url": filename
            }), 200

        except Exception as e:
            print("Erro inesperado:", str(e))
            return jsonify({"status": 500, "message": "Erro interno do servidor.","erro":str(e)}), 500

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

        # Remove arquivo do Supabase
        try:
            res = supabase.storage.from_("audios").remove([filename])
            print("Supabase remove:", res)
        except Exception as e:
            print("Erro ao remover do Supabase:", e)
            return jsonify({"status": 500, "message": "Erro ao excluir no Supabase."}), 500

        return jsonify({"status": 200, "message": "Áudio excluído com sucesso!"}), 200

    except Exception as e:
        print("Erro inesperado:", str(e))
        return jsonify({"status": 500, "message": "Erro interno do servidor."}), 500

    

# ---------------------------------------------------------
# 🎵 Rota pública para servir áudios
# ---------------------------------------------------------
@app.route('/audio/<filename>')
def serve_audio(filename):
    public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(filename)
    return render_template("player.html", audio_url=public_url)


if __name__ == "__main__":
    app.run(debug=True)








