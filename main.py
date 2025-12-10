from flask import *
from gtts import gTTS
import time
import logging
import urllib.request
import urllib.parse
import os

app = Flask(__name__)

AUDIO_DIR = "audio"

# # Configura proxy da rede (caso necessário)

# Gera arquivo MP3 usando gTTS
def text_to_speech(text):
    path = "audio/audio.mp3"
    
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Remove arquivo anterior
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception as e:
        logging.warning(f"Erro ao remover arquivo anterior: {e}")
    
    # PRIMEIRA TENTATIVA: Versão simplificada (compatível com Render)
    try:
        tts = gTTS(text=text, lang="pt", slow=False)
        tts.save(path)
        return path
        
    except Exception as e:
        logging.error(f"Primeira tentativa falhou: {e}")
        
        # SEGUNDA TENTATIVA: Usar método alternativo sem session
        try:
            # Versão usando apenas o gTTS básico
            tts = gTTS(text=text, lang="pt")
            tts.save(path)
            return path
            
        except Exception as e2:
            logging.error(f"Segunda tentativa falhou: {e2}")
            
            # TERCEIRA TENTATIVA: Download direto do Google TTS
            try:
                # Formata o texto para URL
                import urllib.parse
                text_encoded = urllib.parse.quote(text)
                
                # URL do Google TTS
                url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text_encoded}&tl=pt-BR&client=tw-ob"
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(url, headers=headers, timeout=30)
                
                if response.status_code == 200:
                    with open(path, 'wb') as f:
                        f.write(response.content)
                    return path
                else:
                    raise Exception(f"Google TTS retornou status: {response.status_code}")
                    
            except Exception as e3:
                logging.error(f"Terceira tentativa falhou: {e3}")
                
                # ÚLTIMA TENTATIVA: Gerar áudio offline (se pyttsx3 estiver instalado)
                try:
                    return generate_audio_offline(text, path)
                except:
                    raise Exception(f"Todas as tentativas falharam. Último erro: {e3}")

def generate_audio_offline(text, path):
    """Fallback offline usando pyttsx3 se disponível"""
    try:
        import pyttsx3
        
        engine = pyttsx3.init()
        
        # Configurações para português
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'portuguese' in voice.name.lower() or 'português' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        
        # Salvar em arquivo
        engine.save_to_file(text, path)
        engine.runAndWait()
        
        return path
        
    except ImportError:
        raise Exception("pyttsx3 não está instalado. Adicione ao requirements.txt")
    except Exception as e:
        raise Exception(f"Erro no pyttsx3: {e}")


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



@app.route("/excluir_audio", methods=["GET", "POST"])
def excluir_audio():
    if request.method == 'POST':
        dados = request.get_json()
        excluir = dados[0].get('excluir')
        path = "audio/audio.mp3"

        try:
            if excluir:
                if os.path.exists(path):
                    os.remove(path)

                return jsonify({"status": 200, "message": "Áudio excluído com sucesso!."}), 200

        except (KeyError, TypeError) as e:
            print("Erro nos dados recebidos:", str(e))
            return jsonify({"status": 500, "message": "Erro ao excluir o áudio."}), 500
        
        except Exception as e:
            print("Erro inesperado:", str(e))
            return jsonify({"status": 500, "message": "Erro interno do servidor."}), 500
            


@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)


if __name__ == "__main__":
    app.run(debug=True)


