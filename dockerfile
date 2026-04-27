FROM python:3.9-slim

WORKDIR /app

# Copiamos solo los requerimientos primero para aprovechar el cache de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Luego copiamos el resto del código
COPY . .

# Comando para ejecutar (puedes cambiarlo a pytest para que la nube valide todo al iniciar)
CMD ["python", "main.py"]