from dataclasses import dataclass


@dataclass
class VegetationIndices:
    ndvi: float
    evi: float
    ndmi: float


def normalize(value: float, min_value: float = -1.0, max_value: float = 1.0) -> float:
    clipped = min(max(value, min_value), max_value)
    return (clipped - min_value) / (max_value - min_value)


def biomass_score(indices: VegetationIndices) -> float:
    ndvi_n = normalize(indices.ndvi)
    evi_n = normalize(indices.evi)
    ndmi_n = normalize(indices.ndmi)
    return (0.45 * ndvi_n) + (0.35 * evi_n) + (0.20 * ndmi_n)


def biomass_category(score: float) -> str:
    if score < 0.2:
        return "Very Low"
    if score < 0.4:
        return "Low"
    if score < 0.6:
        return "Medium"
    if score < 0.8:
        return "High"
    return "Very High"
