from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.entities import SensorReading, MarketPrice, Forecast, Sensor, GrapeVariety, PredictiveModel, Alert

class SQLSensorReadingRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def find_by_period(self, start, end, variety_id=None):
        q = select(SensorReading).where(SensorReading.measured_at >= start, SensorReading.measured_at <= end)
        if variety_id is not None: q = q.where(SensorReading.variety_id == variety_id)
        result = await self.session.execute(q.order_by(SensorReading.measured_at.asc()))
        return list(result.scalars().all())
    async def save_many(self, readings):
        objects = [SensorReading(**row) for row in readings]
        self.session.add_all(objects)
        await self.session.flush()
        return len(objects)

class SQLMarketPriceRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def find_by_period(self, start, end, variety_id=None):
        q = select(MarketPrice).where(MarketPrice.reference_date >= start, MarketPrice.reference_date <= end)
        if variety_id is not None: q = q.where(MarketPrice.variety_id == variety_id)
        result = await self.session.execute(q.order_by(MarketPrice.reference_date.asc()))
        return list(result.scalars().all())

class SQLForecastRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def save_many(self, forecasts):
        objects = [Forecast(**row) for row in forecasts]
        self.session.add_all(objects)
        await self.session.flush()
        return len(objects)
    async def find_latest(self, variety_id=None):
        q = select(Forecast)
        if variety_id is not None: q = q.where(Forecast.variety_id == variety_id)
        result = await self.session.execute(q.order_by(Forecast.generated_at.desc()))
        return list(result.scalars().all())

class SQLSensorRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def find_by_code(self, code):
        result = await self.session.execute(select(Sensor).where(Sensor.code == code))
        return result.scalar_one_or_none()

class SQLGrapeVarietyRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def find_by_name(self, name):
        result = await self.session.execute(select(GrapeVariety).where(GrapeVariety.name == name))
        return result.scalar_one_or_none()

class SQLPredictiveModelRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def find_by_status(self, status):
        result = await self.session.execute(select(PredictiveModel).where(PredictiveModel.status == status))
        return list(result.scalars().all())

class SQLAlertRepository:
    def __init__(self, session: AsyncSession): self.session = session
    async def find_active(self, category=None):
        q = select(Alert).where(Alert.resolved.is_(False))
        if category: q = q.where(Alert.category == category)
        result = await self.session.execute(q.order_by(Alert.created_at.desc()))
        return list(result.scalars().all())
