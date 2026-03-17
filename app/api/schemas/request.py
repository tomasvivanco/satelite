from typing import Literal

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    input_type: Literal["coordinates", "place_name", "geojson", "kml"]
    location_query: str | None = Field(default=None, description="Place name query")
    latitude: float | None = None
    longitude: float | None = None
    geometry: dict | None = Field(default=None, description="GeoJSON polygon/multipolygon")
    start_date: str | None = "2024-01-01"
    end_date: str | None = "2024-12-31"
    max_cloud_cover: float = 20.0


class UploadAOIRequest(BaseModel):
    geometry: dict
    name: str = "uploaded-aoi"
