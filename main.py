from flask import *
from gtts import gTTS
import time
import os

app = Flask(__name__)

AUDIO_DIR = "audio"

# # Configura proxy da rede (caso necessário)

# Gera arquivo MP3 usando gTTS
def text_to_speech(text):
    path = "audio/audio.mp3"
    
    # Remove arquivo anterior
    try:
        if os.path.exists(path):
            os.remove(path)
    except:
        pass
    
    try:
        import requests
        from gtts import gTTS
        
        # Criar uma sessão customizada
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Criar o objeto gTTS com a sessão customizada
        tts = gTTS(
            text=text, 
            lang="pt", 
            slow=False,
            session=session  # Passar a sessão diretamente
        )
        
        # Salvar o arquivo
        tts.save(path)
        
    except Exception as e:
        # Fallback: tentar sem sessão customizada
        try:
            tts = gTTS(text=text, lang="pt", slow=False)
            tts.save(path)
        except Exception as fallback_error:
            raise Exception(f"Falha principal: {str(e)}, Fallback também falhou: {str(fallback_error)}")
    
    return path


@app.route("/home", methods=["GET", "POST"])
def home():
    audio_files = []
    if os.path.exists(AUDIO_DIR):
        audio_files = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.mp3')]

    return render_template("home.html", voices=[], audio_files=audio_files)


@app.route("/getText", methods=["GET", "POST"])
def getText():
    if request.method == 'POST':
        try:
            dados = request.get_json()
            texto = dados[0].get('texto')

            # Validação
            if not texto:
                return jsonify({"status": 400, "message": "Texto não pode estar vazio."}), 400

            # Converte texto → áudio
            path = text_to_speech(texto)

            print("Texto convertido com sucesso!")
            return jsonify({
                "status": 200,
                "message": "Texto convertido com sucesso.",
                "audio_url": "/audio/audio.mp3"
            }), 200

        except Exception as e:
            print("Erro inesperado:", str(e))
            return jsonify({"status": 500, "message": "Erro interno do servidor."}), 500

    return jsonify({"status": 405, "message": "Método não permitido."}), 405


@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)


if __name__ == "__main__":
    app.run(debug=True)
