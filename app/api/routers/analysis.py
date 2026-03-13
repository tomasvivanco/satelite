from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.api.schemas.request import AnalysisRequest, UploadAOIRequest
from app.api.schemas.response import AnalysisMetrics, AnalysisResponse
from app.api.services.classification_service import classify_land_cover
from app.api.services.ecology_service import infer_ecoregion
from app.api.services.gee_service import fetch_sentinel2_indices
from app.api.services.georef_service import geocode_place
from app.api.services.index_service import biomass_category, biomass_score
from app.api.services.llm_service import generate_interpretation

router = APIRouter(prefix="/analysis", tags=["analysis"])

ANALYSIS_STORE: dict[str, AnalysisResponse] = {}


@router.post("/run", response_model=AnalysisResponse)
def run_analysis(payload: AnalysisRequest) -> AnalysisResponse:
    lat, lon = payload.latitude, payload.longitude

    if payload.input_type == "place_name":
        if not payload.location_query:
            raise HTTPException(status_code=400, detail="location_query is required")
        lat, lon = geocode_place(payload.location_query)

    if lat is None or lon is None:
        raise HTTPException(status_code=400, detail="latitude and longitude are required")

    indices = fetch_sentinel2_indices(lat, lon)
    land_cover = classify_land_cover(indices.ndvi, indices.ndmi)
    bio_score = biomass_score(indices)
    eco, biome = infer_ecoregion(lat, lon)

    metrics = AnalysisMetrics(
        ndvi=indices.ndvi,
        evi=indices.evi,
        ndmi=indices.ndmi,
        biomass_score=bio_score,
        biomass_category=biomass_category(bio_score),
        land_cover=dict(land_cover),
        ecoregion=eco,
        biome=biome,
    )

    analysis_id = str(uuid4())
    response = AnalysisResponse(
        analysis_id=analysis_id,
        status="completed",
        metrics=metrics,
        interpretation=generate_interpretation(metrics),
    )
    ANALYSIS_STORE[analysis_id] = response
    return response


@router.post("/upload-aoi")
def upload_aoi(payload: UploadAOIRequest) -> dict[str, str]:
    return {"status": "accepted", "name": payload.name}


@router.get("/{analysis_id}", response_model=AnalysisResponse)
def get_analysis(analysis_id: str) -> AnalysisResponse:
    if analysis_id not in ANALYSIS_STORE:
        raise HTTPException(status_code=404, detail="analysis not found")
    return ANALYSIS_STORE[analysis_id]


@router.get("/{analysis_id}/map")
def get_analysis_map(analysis_id: str) -> dict[str, str]:
    if analysis_id not in ANALYSIS_STORE:
        raise HTTPException(status_code=404, detail="analysis not found")
    return {"analysis_id": analysis_id, "map_url": f"/maps/{analysis_id}.png"}


@router.get("/{analysis_id}/metrics")
def get_analysis_metrics(analysis_id: str) -> AnalysisMetrics:
    if analysis_id not in ANALYSIS_STORE:
        raise HTTPException(status_code=404, detail="analysis not found")
    return ANALYSIS_STORE[analysis_id].metrics  # type: ignore[return-value]
