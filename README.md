# 🧠 API Predict

Mini API FastAPI servant de base qui illustre comment transformer un modèle Python simple en service web conteneurisé.

---

## 🚀 Fonctionnement

Le service expose deux endpoints :
- **GET /health** → vérifie que l’API est opérationnelle (`{"status": "ok"}`)
- **POST /predict** → renvoie une prédiction simple à partir d’un input `x` (`y = 2x + 1`)

---

## 🧩 Exécution en local

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer l’API
```bash
uvicorn app.main:app --reload
```

### 3. Tester
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → interface Swagger  
- Exemple requête :
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"x": 3}'
```

Résultat attendu :
```json
{"prediction": 7}
```

---

## 🐳 Exécution avec Docker

### 1. Construire l’image
```bash
docker build -t api_predict .
```

### 2. Lancer le conteneur
```bash
docker run -p 8000:8000 api_predict
```

### 3. Vérifier le fonctionnement
```bash
curl http://127.0.0.1:8000/health
```

---

## 📦 Structure du projet

```
api_predict/
├─ app/
│  ├─ __init__.py
│  └─ main.py
├─ requirements.txt
├─ Dockerfile
└─ README.md
```

---

## Qualité du code
Ce projet utilise :
- **Ruff** pour le linting (`ruff check .`)
- **Black** pour le formatage (`black .`)

## 🚀 CI/CD

Le projet utilise GitHub Actions pour :
- ✅ Vérification de la qualité du code (Ruff + Black)
- ✅ Exécution des tests unitaires (pytest)
- ✅ Construction de l'image Docker (ARM64)

Le workflow se déclenche automatiquement sur chaque push et pull request.

---

## ✅ Prochaine étape

Intégrer le tracking et monitoring avec **MLflow** pour :
- Suivre les métriques et paramètres du modèle
- Gérer les versions des modèles
- Monitorer les performances en production