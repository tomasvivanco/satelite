from collections.abc import Mapping


def classify_land_cover(ndvi: float, ndmi: float) -> Mapping[str, float]:
    """
    Basic heuristic baseline for MVP.
    Values represent area proportion.
    """
    vegetation = max(0.0, min(1.0, (ndvi + 1) / 2))
    moisture = max(0.0, min(1.0, (ndmi + 1) / 2))
    water = round((1 - vegetation) * moisture * 0.4, 3)
    forest = round(vegetation * 0.5, 3)
    shrubland = round(vegetation * 0.3, 3)
    bare = round(max(0.0, 1 - (water + forest + shrubland)), 3)
    return {
        "forest": forest,
        "shrubland": shrubland,
        "water": water,
        "bare_or_built": bare,
    }
