from datetime import datetime
from app.integrations.thingspeak_client import ThingSpeakClient
from app.services.data_quality_service import DataQualityService

class ThingSpeakIngestionService:
    def __init__(self, reading_repository=None):
        self.client = ThingSpeakClient()
        self.repository = reading_repository
        self.quality = DataQualityService()

    async def sync(self, sensor_id: int, variety_id: int | None = None):
        feeds = await self.client.fetch_feeds()
        normalized = []
        rejected = []
        for feed in feeds:
            row = {
                "sensor_id": sensor_id,
                "variety_id": variety_id,
                "measured_at": datetime.fromisoformat(feed["created_at"].replace("Z", "+00:00")),
                "temperature_c": self._float_or_none(feed.get("field1")),
                "humidity_pct": self._float_or_none(feed.get("field2")),
                "source_feed_id": str(feed.get("entry_id", "")),
            }
            validation = self.quality.validate_reading(row)
            if validation["valid"]:
                normalized.append(row)
            else:
                rejected.append({"entry_id": feed.get("entry_id"), "errors": validation["errors"]})
        saved = await self.repository.save_many(normalized) if self.repository and normalized else 0
        return {"received": len(feeds), "normalized": len(normalized), "saved": saved, "rejected": rejected}

    @staticmethod
    def _float_or_none(value):
        try: return float(value) if value not in (None, "") else None
        except (ValueError, TypeError): return None
