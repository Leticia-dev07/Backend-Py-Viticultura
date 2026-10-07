class MarketService:
    def __init__(self, market_repository=None):
        self.repository = market_repository

    async def get_summary(self, variety_id, start, end):
        if not self.repository:
            return {"variety_id": variety_id, "price": None, "price_history": [], "demand_level": "UNKNOWN"}
        rows = await self.repository.find_by_period(start, end, variety_id)
        return {
            "variety_id": variety_id,
            "price": rows[-1].price_brl_kg if rows else None,
            "price_history": [{"timestamp": r.reference_date, "value": r.price_brl_kg} for r in rows],
            "demand_level": "UNKNOWN",
        }
