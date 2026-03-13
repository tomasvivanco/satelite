def infer_ecoregion(latitude: float, longitude: float) -> tuple[str, str]:
    """Simple geographic stub for MVP scaffolding."""
    if -15 <= latitude <= 15:
        return "Tropical Moist Broadleaf Forests", "Tropical Forest"
    if abs(latitude) > 45:
        return "Boreal Forests/Taiga", "Boreal"
    if longitude < -30:
        return "Temperate Broadleaf and Mixed Forests", "Temperate"
    return "Mediterranean Forests, Woodlands and Scrub", "Mediterranean"
