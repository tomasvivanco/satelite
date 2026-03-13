from fastapi import APIRouter, Query

from app.api.services.ecology_service import infer_ecoregion
from app.api.services.georef_service import geocode_place

router = APIRouter(prefix="/ecology", tags=["ecology"])


@router.get("/ecoregion")
def get_ecoregion(
    latitude: float | None = Query(default=None),
    longitude: float | None = Query(default=None),
    place_name: str | None = Query(default=None),
) -> dict[str, str]:
    lat, lon = latitude, longitude

    if place_name and (lat is None or lon is None):
        lat, lon = geocode_place(place_name)

    if lat is None or lon is None:
        lat, lon = 0.0, 0.0

    ecoregion, biome = infer_ecoregion(lat, lon)
    return {"ecoregion": ecoregion, "biome": biome}
