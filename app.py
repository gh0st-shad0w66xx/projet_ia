from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import pandas as pd
import traceback
import joblib
import os

app = FastAPI(
    title="House Price Prediction API",
    description="API pour prédire les prix immobiliers avec un pipeline complet",
    version="1.0.0"
)

# ============================
# 🔥  FIX CORS POUR HTML LOCAL
# ============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Autorise toutes les origines (HTML local, Cloud Run, etc)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "./best_model.pkl"

# Charger le modèle au démarrage
model = None

@app.on_event("startup")
def startup_event():
    global model
    try:
        model = joblib.load(MODEL_PATH)
        print(f"Modèle chargé : {MODEL_PATH}")
    except Exception as e:
        print(f"Erreur chargement modèle : {e}")
        traceback.print_exc()

@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None
    }

@app.post("/predict")
def predict(items: List[Dict[str, Any]]):
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    try:
        df = pd.DataFrame(items)

        if df.empty:
            raise ValueError("Données vides")

        # Le preprocess est déjà dans le pipeline → on prédit direct
        preds = model.predict(df)

        return {
            "predictions": preds.tolist(),
            "count": len(preds),
            "status": "success"
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erreur serveur : {e}")

@app.get("/")
def root():
    return {"message": "API de prédiction des prix immobiliers. Voir /docs pour tester."}
