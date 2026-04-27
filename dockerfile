FROM python:3.9-slim

WORKDIR /app

# Instalamos dependencias primero para optimizar el cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Al ejecutar el contenedor, mostrará los datos limpios
CMD ["python", "main.py"]