from datetime import datetime
from pydantic import BaseModel, Field

class PeriodDto(BaseModel):
    start: datetime | None = None
    end: datetime | None = None

class MetricDto(BaseModel):
    label: str
    value: str
    unit: str | None = None
    trend: str | None = None

class TimeSeriesPointDto(BaseModel):
    timestamp: datetime
    value: float

class RecommendationDto(BaseModel):
    title: str
    recommendation_type: str
    description: str
    confidence: float = Field(ge=0, le=1)
    created_at: datetime | None = None

class DashboardOverviewResponse(BaseModel):
    variety: str
    period: PeriodDto
    metrics: list[MetricDto]
    temperature_series: list[TimeSeriesPointDto]
    humidity_series: list[TimeSeriesPointDto]
    recommendations: list[RecommendationDto]
    risk_level: str

class MonitoringResponse(BaseModel):
    sensors: list[dict]
    latest_readings: list[dict]
    temperature_series: list[TimeSeriesPointDto]
    humidity_series: list[TimeSeriesPointDto]
    recent_alerts: list[dict]

class ReadingResponse(BaseModel):
    reading_id: int
    timestamp: datetime
    temperature: float | None
    humidity: float | None
    sensor_code: str
    variety: str | None
    status: str

class MarketResponse(BaseModel):
    price: float | None
    price_history: list[TimeSeriesPointDto]
    demand_level: str
    variety: str

class ForecastResponse(BaseModel):
    variety: str
    generated_at: datetime
    predictions: list[TimeSeriesPointDto]
    risk_level: str
    recommendations: list[RecommendationDto]
    model_version: str

class DataQualityResponse(BaseModel):
    completeness: float
    consistency: float
    valid_count: int
    invalid_count: int
    missing_count: int
    outlier_count: int

class ModelMetricResponse(BaseModel):
    name: str
    version: str
    accuracy: float | None
    mae: float | None
    rmse: float | None
    status: str

class AlertResponse(BaseModel):
    id: int
    category: str
    level: str
    title: str
    message: str
    created_at: datetime

class VarietySummaryDto(BaseModel):
    name: str
    score: float
    temperature: float | None = None
    humidity: float | None = None
    market_price: float | None = None
    risk: str
