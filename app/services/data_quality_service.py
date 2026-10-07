class DataQualityService:
    def validate_reading(self, reading: dict) -> dict:
        errors = []
        temp = reading.get("temperature_c")
        humidity = reading.get("humidity_pct")
        if temp is None: errors.append("temperature_missing")
        elif temp < -10 or temp > 60: errors.append("temperature_out_of_range")
        if humidity is None: errors.append("humidity_missing")
        elif humidity < 0 or humidity > 100: errors.append("humidity_out_of_range")
        return {"valid": not errors, "errors": errors}

    def calculate_quality(self, readings: list[dict]) -> dict:
        if not readings:
            return {"completeness": 0.0, "consistency": 0.0, "valid_count": 0,
                    "invalid_count": 0, "missing_count": 0, "outlier_count": 0}
        checks = [self.validate_reading(row) for row in readings]
        valid = sum(item["valid"] for item in checks)
        missing = sum("temperature_missing" in item["errors"] or "humidity_missing" in item["errors"] for item in checks)
        return {
            "completeness": round(1 - missing / len(readings), 4),
            "consistency": round(valid / len(readings), 4),
            "valid_count": valid,
            "invalid_count": len(readings) - valid,
            "missing_count": missing,
            "outlier_count": sum(any("out_of_range" in err for err in item["errors"]) for item in checks),
        }
