from pathlib import Path
import joblib
from app.core.config import settings

class MLPredictionClient:
    def __init__(self, artifact_name: str = "agroclima_model.joblib"):
        self.artifact_path = Path(settings.MODEL_DIR) / artifact_name

    def predict(self, features: list[list[float]]) -> list[float]:
        if not self.artifact_path.exists():
            raise FileNotFoundError("Modelo treinado não encontrado")
        model = joblib.load(self.artifact_path)
        return model.predict(features).tolist()
