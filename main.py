from flask import *
import pyttsx3
import time
import os

app = Flask(__name__)

AUDIO_DIR = "audio"

def text_to_speech(text, voice_index):
    path = "audio/audio.wav"

    # Remove o arquivo se já existir, para evitar bloqueio
    try:
        if os.path.exists(path):
            os.remove(path)
    except:
        pass  # Se estiver em uso, o Windows pode dar erro — ignoramos

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    voices = engine.getProperty('voices')
    if 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)

    engine.save_to_file(text, path)
    engine.runAndWait()
    engine.stop()



@app.route("/home", methods=["GET", "POST"])
def home():
    # Pega as vozes
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Lê a pasta de áudios
    audio_files = []
    if os.path.exists(AUDIO_DIR):
        audio_files = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.wav')]

    return render_template("home.html", voices=voices, audio_files=audio_files)

    
    
# Home page route
@app.route("/getText", methods=["GET", "POST"])
def getText():
    if request.method == 'POST':
        try:
            dados = request.get_json()
            texto = dados[0].get('texto')
            voice = dados[0].get('voice', 0)  # Valor padrão caso não seja fornecido
            
            # Valida se o texto foi enviado
            if not texto:
                return jsonify({"status": 400, "message": "Texto não pode estar vazio."}), 400
            
            # Valida o índice da voz
            try:
                voice_index = int(voice)
            except ValueError:
                return jsonify({"status": 400, "message": "Seleção de voz inválida."}), 400
            
            # Chamada da função de conversão de texto em fala
            text_to_speech(texto, voice_index)  # Função externa
            
            print("Texto convertido com sucesso!")
            # Retorna a URL do áudio gerado
            return jsonify({"status": 200, "message": "Texto convertido com sucesso.", "audio_url": "/audio/audio.wav"}), 200
        
        except (KeyError, TypeError) as e:
            print("Erro nos dados recebidos:", str(e))
            return jsonify({"status": 500, "message": "Erro no processamento dos dados recebidos."}), 500
        
        except Exception as e:
            print("Erro inesperado:", str(e))
            return jsonify({"status": 500, "message": "Erro interno do servidor."}), 500
    
    # Retorno padrão para GET (caso necessário)
    return jsonify({"status": 405, "message": "Método não permitido."}), 405


@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)

        



if __name__ == "__main__":
    app.run(debug=True)