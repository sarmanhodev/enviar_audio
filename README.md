# Text-to-Speech Converter

Este repositório contém uma aplicação web que converte texto em áudio usando Python no backend e um frontend moderno e responsivo.

## 📋 Funcionalidades

- Interface simples para inserir texto e ouvir o áudio gerado.
- Suporte para diferentes vozes e velocidades (se configurado no backend).
- Converte texto em áudio instantaneamente.
- Frontend responsivo e amigável.

## 🛠️ Tecnologias Utilizadas

### Backend:
- **Python**
  - `Flask`: Framework web usado para criar a API.
  - `GTTS`: Biblioteca para conversão de texto em áudio.

### Frontend:
- **HTML5**, **CSS3**, **JavaScript**
- **Bootstrap**: Para um design responsivo.
- **jQuery**: Para manipulação do DOM e chamadas AJAX.

## 🚀 Como Rodar o Projeto

### Pré-requisitos:
- Python 3.8 ou superior.
- Node.js (opcional, para gerenciar dependências frontend, se necessário).

### Passos:
1. Clone este repositório:
   ```bash
   git clone https://github.com/sarmanhodev/enviar_audio.git
   cd enviar_audio


2. Instale as dependências do backend:
  pip install flask gtts eventlet gunicorn

3. Inicie o servidor:
  python main.py
  O servidor será executado em http://127.0.0.1:5000/home


🗂️ Estrutura do Projeto
.
├── main.py                # Código principal do backend
├── audio/                
    └── audio.mp3
├── static/
│   ├── css/
│   │   └── styles.css    # Arquivo CSS customizado
│   ├── js/
│       └── functions.js     # Funções JavaScript e integração com API
│       └── script.js     # Funções JavaScript e integração com API
├── templates/
│   └── index.html        # Página principal
└── README.md             # Documentação do projeto



🌟 Exemplos de Uso
  1.Abra a página no navegador.
  2.Digite o texto que deseja converter.
  3.Clique no botão "Converter" para gerar o arquivo de áudio
  4.Clique no botão verde para enviar o arquivo para um número de WhatsApp

  
Desenvolvido por Diego Sarmanho

