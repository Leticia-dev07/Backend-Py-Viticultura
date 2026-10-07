from app.services.data_quality_service import DataQualityService

class AnalyticsService:
    def __init__(self, reading_service=None):
        self.reading_service = reading_service
        self.quality_service = DataQualityService()

    async def get_data_quality(self, readings_as_dicts: list[dict]):
        return self.quality_service.calculate_quality(readings_as_dicts)

    async def get_variety_summary(self, summaries: list[dict]):
        return sorted(summaries, key=lambda item: item.get("score", 0), reverse=True)
