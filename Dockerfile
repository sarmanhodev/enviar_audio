FROM python:3.11-slim

WORKDIR /app

# Copia apenas requirements primeiro (melhor cache)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Agora copia o resto do projeto
COPY . .

EXPOSE 8000

CMD ["gunicorn", "-k", "eventlet", "-w", "1", "main:app", "-b", "0.0.0.0:8000"]
