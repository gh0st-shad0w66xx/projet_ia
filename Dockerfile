FROM python:3.11-slim

WORKDIR /app

# Installer dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'API
COPY . .

# Cloud Run exige le port 8080
EXPOSE 8080

# Lancer FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
