import httpx
from app.core.config import settings

class ThingSpeakClient:
    async def fetch_feeds(self, results: int | None = None) -> list[dict]:
        if not settings.THINGSPEAK_CHANNEL_ID:
            return []
        params = {"results": results or settings.THINGSPEAK_RESULTS}
        if settings.THINGSPEAK_READ_API_KEY:
            params["api_key"] = settings.THINGSPEAK_READ_API_KEY
        url = f"{settings.THINGSPEAK_BASE_URL}/channels/{settings.THINGSPEAK_CHANNEL_ID}/feeds.json"
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            payload = response.json()
        return payload.get("feeds", [])
