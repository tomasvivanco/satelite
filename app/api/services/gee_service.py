from app.api.services.index_service import VegetationIndices


def fetch_sentinel2_indices(latitude: float, longitude: float) -> VegetationIndices:
    """
    Placeholder for Sentinel-2 + cloud masking processing.
    Returns deterministic pseudo-values to support MVP integration wiring.
    """
    ndvi = max(-1.0, min(1.0, 0.5 - (abs(latitude) / 180)))
    evi = max(-1.0, min(1.0, 0.4 - (abs(longitude) / 360)))
    ndmi = max(-1.0, min(1.0, (ndvi + evi) / 2))
    return VegetationIndices(ndvi=ndvi, evi=evi, ndmi=ndmi)
