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
  - `pyttsx3`: Biblioteca para conversão de texto em áudio.

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
   git clone https://github.com/sarmanhodev/text_to_audio.git
   cd text_to_audio


2. Instale as dependências do backend:
  pip install flask pyttsx3

3. Inicie o servidor:
  python app.py
  O servidor será executado em http://127.0.0.1:5000


🗂️ Estrutura do Projeto
.
├── app.py                # Código principal do backend
├── static/
│   ├── css/
│   │   └── styles.css    # Arquivo CSS customizado
│   ├── js/
│   │   └── script.js     # Funções JavaScript e integração com API
│   └── bootstrap/        # Arquivos do Bootstrap
├── templates/
│   └── index.html        # Página principal
└── README.md             # Documentação do projeto




Aqui está um exemplo de README.md para o seu projeto:

markdown
Copiar código
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
  - `pyttsx3`: Biblioteca para conversão de texto em áudio.

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
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
Instale as dependências do backend:

bash
Copiar código
pip install flask pyttsx3
Inicie o servidor:

bash
Copiar código
python app.py
O servidor será executado em http://127.0.0.1:5000.

Abra o arquivo index.html no navegador ou utilize o servidor Flask para servir os arquivos estáticos.

🗂️ Estrutura do Projeto
csharp
Copiar código
.
├── app.py                # Código principal do backend
├── static/
│   ├── css/
│   │   └── styles.css    # Arquivo CSS customizado
│   ├── js/
│   │   └── script.js     # Funções JavaScript e integração com API
│   └── bootstrap/        # Arquivos do Bootstrap
├── templates/
│   └── index.html        # Página principal
└── README.md             # Documentação do projeto


🌟 Exemplos de Uso
  1.Abra a página no navegador.
  2.Digite o texto que deseja converter.
  3.Clique no botão "Converter" para ouvir o áudio gerado.

  
⚙️ Configuração Adicional
  Alterar Voz e Velocidade:
  No arquivo app.py, você pode configurar as propriedades da voz e velocidade usando o pyttsx3. Exemplo:
  engine = pyttsx3.init()
  engine.setProperty('rate', 150)  # Velocidade
  engine.setProperty('voice', voices[1].id)  # Alterar a voz (se disponível)


Desenvolvido por Diego Sarmanho

