from pydantic import BaseModel


class AnalysisMetrics(BaseModel):
    ndvi: float
    evi: float
    ndmi: float
    biomass_score: float
    biomass_category: str
    land_cover: dict[str, float]
    ecoregion: str
    biome: str


class AnalysisResponse(BaseModel):
    analysis_id: str
    status: str
    metrics: AnalysisMetrics | None = None
    interpretation: str | None = None
