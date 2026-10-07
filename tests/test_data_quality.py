from app.services.data_quality_service import DataQualityService

def test_validate_valid_reading():
    result = DataQualityService().validate_reading({"temperature_c": 25.0, "humidity_pct": 60.0})
    assert result["valid"] is True

def test_validate_invalid_humidity():
    result = DataQualityService().validate_reading({"temperature_c": 25.0, "humidity_pct": 130.0})
    assert result["valid"] is False
