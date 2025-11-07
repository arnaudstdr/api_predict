# Image de base optimisé pour le dev Python sous VSCode
FROM mcr.microsoft.com/devcontainers/python:3.11

# Installe outils système utiles au MLOps
RUN apt-get update && apt-get install -y \
    git curl make docker-cli \
    && apt-get clean

# Mise à jour pip + outils modernes
RUN pip install --upgrade pip setuptools wheel poetry

# Librairies typiques ML/MLOps
RUN pip install \
    numpy pandas scikit-learn matplotlib seaborn \
    fastapi uvicorn[standard] jupyterlab \
    mlflow pydantic requests rich \
    torch torchvision torchaudio \
    black ruff

# Répertoire de travail
WORKDIR /workspace