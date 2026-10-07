# AgroClima Cloud — Backend Python conforme diagrama de classes

Este projeto implementa a camada de análise de dados, dashboards, integrações ThingSpeak/ML, previsões e alertas.
Autenticação, autorização, gestão de usuários e RBAC continuam no backend Java.

## Arquitetura por camadas
- `api/controllers`: DashboardController, ForecastController, AnalyticsController, AlertController
- `services`: DashboardService, ReadingService, DataQualityService, ForecastService, ThingSpeakIngestionService, MarketService, AlertService, ModelService
- `integrations`: ThingSpeakClient e MLPredictionClient
- `repositories`: consultas e persistência
- `models`: Sensor, SensorReading, GrapeVariety, MarketPrice, PredictiveModel, Forecast, Alert e enums
- `schemas`: DTOs de request/response para o frontend
- `database`: sessão SQLAlchemy

## Stack
FastAPI, SQLAlchemy async, PostgreSQL, Pydantic, httpx, pandas, scikit-learn, joblib.

## Executar (Windows)
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```
Swagger: http://localhost:8000/docs

## Atenção
A estrutura está pronta para integração, mas as consultas dos repositories e parte das regras de negócio são esqueleto inicial. Os dados do dashboard devem vir do banco/ThingSpeak/modelos reais; os valores de exemplo não são dados de produção.
