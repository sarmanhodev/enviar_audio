# 🗣️ Text-to-Speech Converter (Flask + gTTS + Supabase)

Aplicação web para converter texto em áudio (MP3) usando **Python/Flask**, **gTTS** e **Supabase Storage**.

---

## 📌 Funcionalidades

- Conversão de texto em áudio (voz PT-BR)
- Upload automático para Supabase Storage
- Retorno de URL pública
- Envio via WhatsApp
- Interface moderna e responsiva

---

## 🚀 Fluxo de Funcionamento

1. O usuário digita um texto na interface.  
2. O backend gera um arquivo MP3 temporário usando gTTS.  
3. O arquivo é enviado automaticamente para o bucket Supabase.  
4. O arquivo temporário local é deletado.  
5. O Supabase retorna uma URL pública, que é enviada ao frontend.  
6. O usuário pode:  
   - ouvir o áudio  
   - baixar  
   - enviar via WhatsApp  

---

## 🛠 Tecnologias Utilizadas

### Backend
- Python 3  
- Flask  
- gTTS  
- Supabase Python Client  
- Eventlet + Gunicorn  

### Frontend
- HTML5, CSS3  
- Bootstrap  
- jQuery  

---

## 📦 Estrutura do Projeto

```
.
├── main.py
├── conexao_supabase.py
├── tmp_audio/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
└── README.md
```

---

## ▶️ Como Rodar o Projeto

```bash
git clone https://github.com/sarmanhodev/enviar_audio.git
cd enviar_audio
pip install flask gtts supabase eventlet gunicorn
python main.py
```

Acesse:  
`http://127.0.0.1:5000/home`

---

## 👨‍💻 Desenvolvido por  
**Diego Sarmanho**

