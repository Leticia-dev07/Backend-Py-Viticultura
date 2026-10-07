from pathlib import Path
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from app.core.config import settings

class ModelService:
    async def get_models(self):
        return []

    async def train_baseline(self, X, y, name="AgroClimaRandomForest", version="1.0"):
        if len(X) < 5:
            raise ValueError("São necessários pelo menos cinco exemplos para treino inicial.")
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        predictions = model.predict(X)
        mae = mean_absolute_error(y, predictions)
        rmse = mean_squared_error(y, predictions) ** 0.5
        directory = Path(settings.MODEL_DIR)
        directory.mkdir(parents=True, exist_ok=True)
        artifact = directory / f"{name}_{version}.joblib"
        joblib.dump(model, artifact)
        return {"name": name, "version": version, "mae": float(mae), "rmse": float(rmse), "artifact_path": str(artifact)}
