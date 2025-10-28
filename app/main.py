from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Modèle d'entrée
class InputData(BaseModel):
    x: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: InputData):
    # modèle simple : y = 2x + 1
    y = 2 * data.x + 1
    return {"prediction": y}
