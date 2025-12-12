from supabase import create_client, Client
import os


# -------------------------------
# Configurações Supabase
# -------------------------------
SUPABASE_URL: str = "https://vntljrcwayhvcbxlgbge.supabase.co"
SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZudGxqcmN3YXlodmNieGxnYmdlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU0MzA2ODgsImV4cCI6MjA4MTAwNjY4OH0.aAmRo2kBI1ujmAi_lCtUc0SMaWX2HhLvhKpQfSoZUKY"
BUCKET_NAME = "audios"

# Cria cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# -------------------------------
# Função para upload de áudio
# -------------------------------
def upload_audio(file_path: str, file_name: str) -> str:
    if not os.path.isfile(file_path):
        print(f"Arquivo local não encontrado: {file_path}")
        return ""
    
    try:
        with open(file_path, "rb") as f:
            res = supabase.storage.from_(BUCKET_NAME).upload(file_name, f)
        print(f"Arquivo enviado com sucesso! Path: {res.path}")
        # Retorna link público
        public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(file_name)
        print(f"Link público: {public_url}")
        return public_url
    except Exception as e:
        print("Erro ao enviar arquivo:", e)
        return ""

# -------------------------------
# Função para download de áudio
# -------------------------------
def download_audio(file_name: str, dest_path: str):
    try:
        # Garantir que a pasta de destino existe
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Remover arquivo antigo se existir
        if os.path.exists(dest_path):
            os.remove(dest_path)
        
        data = supabase.storage.from_(BUCKET_NAME).download(file_name)
        with open(dest_path, "wb") as f:
            f.write(data)
        print(f"Arquivo {file_name} baixado com sucesso em {dest_path}")
    except Exception as e:
        print("Erro ao baixar arquivo:", e)

# -------------------------------
# Função para listar arquivos do bucket
# -------------------------------
def listar_arquivos():
    try:
        files = supabase.storage.from_(BUCKET_NAME).list()
        print("Arquivos no bucket:", [f["name"] for f in files])
    except Exception as e:
        print("Erro ao listar arquivos:", e)

# -------------------------------
# Exemplo de uso
# -------------------------------
# if __name__ == "__main__":
#     # Upload
#     public_url = upload_audio("audio/audio.mp3", "audio1.mp3")
    
#     # Listar arquivos
#     listar_arquivos()
    
#     # Download
#     download_audio("audio1.mp3", "audio/baixado_audio1.mp3")

