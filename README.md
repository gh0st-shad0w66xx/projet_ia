## README – API de Prédiction des Prix Immobiliers

Projet **FastAPI** + Docker + Google Cloud Run

1. Exécuter l’API localement
1) Créer un environnement virtuel :
python -m venv .venv
2) Activer l’environnement (Windows) :
.venv\Scripts\activate
3) Installer les dépendances :
pip install -r requirements.txt
4) Lancer l’API :
uvicorn app:app --reload --host 127.0.0.1 --port 8000
Documentation Swagger : http://127.0.0.1:8000/docs

2. Docker Local
Construire l'image Docker :
docker build -t housing-api .
Exécuter le conteneur :
docker run -p 8000:8000 housing-api
API disponible : http://localhost:8000

3. Rôle des fichiers
Dockerfile : Définit l'environnement et lance Uvicorn.
requirements.txt : Contient toutes les dépendances Python.
best_model.pkl : Pipeline ML complet avec preprocessing + modèle.
app.py : Le code FastAPI (endpoints /health, /predict, /docs).
utils.py : Chargement du modèle.
.dockerignore : Ignore les fichiers inutiles dans le build Docker.

4. Structure du projet
app.py – API FastAPI
utils.py – Fonction load_model
best_model.pkl – Pipeline complet
Dockerfile – Image Docker
requirements.txt – Dépendances
index.html – Interface utilisateur (test API)

5. Déploiement Google Cloud Run
1) Build Cloud Build :
gcloud builds submit --tag gcr.io/api-housing/housing-api

2) Déploiement Cloud Run :
gcloud run deploy housing-api --image gcr.io/api-housing/housing-api --platform managed --region
us-central1 --allow-unauthenticated
URL publique :
https://housing-api-275363795836.us-central1.run.app

6. Tests de l’API
GET /health – Vérification du modèle
POST /predict – Faire une prédiction
/docs – Swagger UI
Exemple JSON :
[
{"MSSubClass": 60,"LotFrontage": 65.0,"LotArea": 8450,"OverallQual": 7,"OverallCond": 5,"YearBuilt": 2003,"YearRemodAdd":
2003,"MasVnrArea": 0.0,"BsmtFinSF1": 706,"BsmtFinSF2": 0,"BsmtUnfSF": 150,"TotalBsmtSF": 856,"1stFlrSF": 856,"2ndFlrSF":
854,"LowQualFinSF": 0,"GrLivArea": 1710,"BsmtFullBath": 1,"BsmtHalfBath": 0,"FullBath": 2,"HalfBath": 1,"BedroomAbvGr":
3,"KitchenAbvGr": 1,"TotRmsAbvGrd": 8,"Fireplaces": 0,"GarageYrBlt": 2003.0,"GarageCars": 2,"GarageArea": 548,"WoodDeckSF":
0,"OpenPorchSF": 61,"EnclosedPorch": 0,"3SsnPorch": 0,"ScreenPorch": 0,"PoolArea": 0,"MiscVal": 0,"MoSold": 2,"YrSold":
2008,"MSZoning": "RL","Street": "Pave","Alley": "NA","LotShape": "Reg","LandContour": "Lvl","Utilities": "AllPub","LotConfig":
"Inside","LandSlope": "Gtl","Neighborhood": "NAmes","Condition1": "Norm","Condition2": "Norm","BldgType": "1Fam","HouseStyle":
"2Story","RoofStyle": "Gable","RoofMatl": "CompShg","Exterior1st": "VinylSd","Exterior2nd": "VinylSd","MasVnrType":
"Stone","ExterQual": "Gd","ExterCond": "TA","Foundation": "PConc","BsmtQual": "Gd","BsmtCond": "TA","BsmtExposure":
"Gd","BsmtFinType1": "GLQ","BsmtFinType2": "Unf","Heating": "GasA","HeatingQC": "Ex","CentralAir": "Y","Electrical":
"SBrkr","KitchenQual": "Gd","Functional": "Typ","FireplaceQu": "NA","GarageType": "Attchd","GarageFinish": "Fin","GarageQual":
"TA","GarageCond": "TA","PavedDrive": "Y","PoolQC": "NA","Fence": "NA","MiscFeature": "NA","SaleType": "WD","SaleCondition":
"Normal"
}
]