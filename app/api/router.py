from fastapi import APIRouter, Depends, Query
from datetime import datetime
from app.core.context import authenticated_context
from app.services.dashboard_service import DashboardService
from app.services.reading_service import ReadingService
from app.services.data_quality_service import DataQualityService
from app.services.alert_service import AlertService
from app.services.analytics_service import AnalyticsService
from app.services.model_service import ModelService
from app.services.thingspeak_client_service import ThingSpeakClientService

router = APIRouter()

@router.get("/dashboard/overview")
async def dashboard_overview(variety: str = "Uva Itália", _ctx=Depends(authenticated_context)):
    return await DashboardService().get_overview(variety)

@router.get("/readings/current")
async def current_readings(_ctx=Depends(authenticated_context)):
    rows = await ReadingService().get_current()
    return [{"timestamp": r.measured_at, "temperature": r.temperature_c, "humidity": r.humidity_pct} for r in rows]

@router.get("/analytics/data-quality")
async def data_quality(_ctx=Depends(authenticated_context)):
    return DataQualityService().calculate_quality([])

@router.get("/alerts")
async def alerts(category: str | None = None, _ctx=Depends(authenticated_context)):
    return await AlertService().list_active(category)

@router.get("/models")
async def models(_ctx=Depends(authenticated_context)):
    return await ModelService().get_models()

@router.get("/integrations/thingspeak/status")
async def thingspeak_status(_ctx=Depends(authenticated_context)):
    return await ThingSpeakClientService().status()
