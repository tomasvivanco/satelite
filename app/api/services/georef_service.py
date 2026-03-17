def geocode_place(place_name: str) -> tuple[float, float]:
    """MVP placeholder geocoder."""
    defaults = {
        "nairobi": (-1.286389, 36.817223),
        "amazonas": (-3.4653, -62.2159),
        "lisbon": (38.7223, -9.1393),
    }
    return defaults.get(place_name.strip().lower(), (0.0, 0.0))
