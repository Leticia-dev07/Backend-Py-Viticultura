from app.core.config import settings

class ThingSpeakClientService:
    async def status(self):
        return {
            "provider": "ThingSpeak",
            "configured": bool(settings.THINGSPEAK_CHANNEL_ID),
            "channel_id": settings.THINGSPEAK_CHANNEL_ID or None,
        }
