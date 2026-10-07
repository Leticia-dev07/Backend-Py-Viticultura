from datetime import datetime, timedelta, timezone
from app.services.reading_service import ReadingService
from app.services.data_quality_service import DataQualityService

class DashboardService:
    def __init__(self, reading_service=None, quality_service=None):
        self.readings = reading_service or ReadingService()
        self.quality = quality_service or DataQualityService()

    async def get_overview(self, variety: str, start=None, end=None):
        rows = await self.readings.get_current()
        # Sem dados reais, retornar listas vazias em vez de inventar métricas.
        if not rows:
            return {
                "variety": variety,
                "period": {"start": start, "end": end},
                "metrics": [],
                "temperature_series": [],
                "humidity_series": [],
                "recommendations": [],
                "risk_level": "UNKNOWN",
                "message": "Sem leituras persistidas para o período.",
            }
        temperatures = [r.temperature_c for r in rows if r.temperature_c is not None]
        humidities = [r.humidity_pct for r in rows if r.humidity_pct is not None]
        return {
            "variety": variety,
            "period": {"start": start, "end": end},
            "metrics": [
                {"label": "Temperatura média", "value": str(round(sum(temperatures)/len(temperatures), 1)), "unit": "°C"} if temperatures else None,
                {"label": "Umidade média", "value": str(round(sum(humidities)/len(humidities), 1)), "unit": "%"} if humidities else None,
            ],
            "temperature_series": [{"timestamp": r.measured_at, "value": r.temperature_c} for r in rows if r.temperature_c is not None],
            "humidity_series": [{"timestamp": r.measured_at, "value": r.humidity_pct} for r in rows if r.humidity_pct is not None],
            "recommendations": [],
            "risk_level": "UNKNOWN",
        }
