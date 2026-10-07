from datetime import datetime, timedelta, timezone
from app.integrations.thingspeak_client import ThingSpeakClient

class ReadingService:
    def __init__(self, reading_repository=None):
        self.repository = reading_repository
        self.thingspeak = ThingSpeakClient()

    async def get_current(self, variety_id=None):
        end = datetime.now(timezone.utc)
        start = end - timedelta(hours=24)
        if self.repository:
            return await self.repository.find_by_period(start, end, variety_id)
        return []

    async def get_period(self, start, end, variety_id=None):
        if self.repository:
            return await self.repository.find_by_period(start, end, variety_id)
        return []
