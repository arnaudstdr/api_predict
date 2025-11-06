from fastapi import FastAPI
from pydantic import BaseModel
from app.train_and_log import train_and_log

app = FastAPI()


# Modèle d'entrée
class Input(BaseModel):
    x: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(inp: Input):
    # modèle simple : y = 2x + 1
    y = train_and_log(inp.x)
    return {"prediction": y}
