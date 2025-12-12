# 🗣️ Text-to-Speech Converter (Flask + gTTS + Supabase)

Aplicação web para converter texto em áudio (MP3) usando Python/Flask, gTTS e Supabase Storage.
O sistema gera o áudio, envia automaticamente para um bucket no Supabase e retorna uma URL pública para download ou reprodução.

#📌 Funcionalidades

Conversão de texto em áudio (voz PT-BR)

Upload automático para Supabase Storage

Retorno de URL pública para ouvir ou compartilhar

Envio opcional do áudio para WhatsApp

Interface simples, moderna e responsiva

Não armazena arquivos em disco (apenas temporariamente)

#🛠 Tecnologias Utilizadas

🔹 Backend

Python 3

Flask

gTTS (Google Text-To-Speech)

Supabase Python Client

Eventlet + Gunicorn (produção)

🔹 Frontend

HTML5, CSS3

Bootstrap

JavaScript + jQuery

AJAX para comunicação com o backend

#🚀 Como Funciona o Processo

O usuário digita um texto na interface.

O backend gera um arquivo MP3 temporário usando gTTS.

O arquivo é enviado automaticamente para o bucket Supabase.

O arquivo temporário local é deletado.

O Supabase retorna uma URL pública, que é enviada ao frontend.

O usuário pode:

ouvir o áudio

baixar

enviar via WhatsApp

#📦 Estrutura do Projeto
.
├── main.py                    # Backend Flask
├── conexao_supabase.py        # Cliente e funções de upload/download
├── tmp_audio/                 # Pasta temporária
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── functions.js
│       └── script.js
├── templates/
│   └── index.html
└── README.md

#🔊 Função Principal (geração + upload)
def text_to_speech(text):
    TMP_AUDIO_DIR = "tmp_audio"
    os.makedirs(TMP_AUDIO_DIR, exist_ok=True)

    filename = f"{uuid.uuid4().hex}.mp3"
    tmp_path = os.path.join(TMP_AUDIO_DIR, filename)

    # Gerar MP3
    tts = gTTS(text=text, lang="pt", slow=False)
    tts.save(tmp_path)

    try:
        public_url = upload_audio(tmp_path, filename)
    except Exception as e:
        raise Exception(f"Erro ao enviar para Supabase: {str(e)}")
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return public_url

#🌐 Função de Upload para o Supabase
def upload_audio(file_path: str, file_name: str) -> str:
    with open(file_path, "rb") as f:
        supabase.storage.from_("audios").upload(file_name, f)

    return supabase.storage.from_("audios").get_public_url(file_name)

#▶️ Como Rodar o Projeto Localmente
1️⃣ Clonar o repositório
git clone https://github.com/sarmanhodev/enviar_audio.git
cd enviar_audio

2️⃣ Instalar dependências
pip install flask gtts supabase eventlet gunicorn

3️⃣ Configurar Supabase

No arquivo conexao_supabase.py:

SUPABASE_URL = "URL_DO_SEU_PROJETO"
SUPABASE_KEY = "SUA_ANON_PUBLIC_KEY"
BUCKET_NAME = "audios"

#4️⃣ Rodar servidor
python main.py


Aplicação disponível em:

http://127.0.0.1:5000/home

#🌟 Como Usar

Acesse a página no navegador.

Digite qualquer texto.

Clique em Converter.

Espere a geração + upload.

Use o link público para:

ouvir

baixar

ou enviar via WhatsApp

#🧪 Endpoints da API (Opcional)
Método	Rota	Descrição
POST	/gerar_audio	Recebe texto e retorna URL pública do MP3
GET	/download/<filename>	Faz download do arquivo (opcional)

#👨‍💻 Desenvolvido por Diego Sarmanho
🔗 GitHub: https://github.com/sarmanhodev
