# Dockerfile
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias y código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto de FastAPI
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "app.interfaces.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]