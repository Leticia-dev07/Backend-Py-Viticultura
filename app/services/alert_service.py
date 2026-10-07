from datetime import datetime, timezone
from app.models.entities import AlertCategory, AlertLevel

class AlertService:
    def __init__(self, alert_repository=None):
        self.repository = alert_repository

    async def list_active(self, category=None):
        if not self.repository:
            return []
        return await self.repository.find_active(category)

    def evaluate_reading(self, temperature_c, humidity_pct):
        alerts = []
        if temperature_c is not None and temperature_c >= 35:
            alerts.append({"category": AlertCategory.CLIMATE.value, "level": AlertLevel.CRITICAL.value,
                           "title": "Temperatura elevada", "message": "Temperatura atingiu ou ultrapassou 35 °C."})
        if humidity_pct is not None and humidity_pct < 35:
            alerts.append({"category": AlertCategory.CLIMATE.value, "level": AlertLevel.WARNING.value,
                           "title": "Umidade baixa", "message": "Umidade abaixo do limite configurado."})
        return alerts
