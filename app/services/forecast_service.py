from datetime import datetime, timedelta, timezone
from app.integrations.ml_prediction_client import MLPredictionClient

class ForecastService:
    def __init__(self, forecast_repository=None):
        self.repository = forecast_repository
        self.ml_client = MLPredictionClient()

    async def get_latest(self, variety_id=None):
        if self.repository:
            return await self.repository.find_latest(variety_id)
        return []

    async def generate_forecast(self, variety_id: int, features: list[list[float]], horizon_hours: int = 24):
        predictions = self.ml_client.predict(features)
        now = datetime.now(timezone.utc)
        return [
            {
                "variety_id": variety_id,
                "generated_at": now,
                "target_at": now + timedelta(hours=(i + 1) * max(1, horizon_hours // max(1, len(predictions)))),
                "predicted_value": value,
            }
            for i, value in enumerate(predictions)
        ]
