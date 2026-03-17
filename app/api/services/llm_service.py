from app.api.schemas.response import AnalysisMetrics


def generate_interpretation(metrics: AnalysisMetrics) -> str:
    observed = (
        f"Observed: vegetation index signals (NDVI={metrics.ndvi:.2f}, "
        f"EVI={metrics.evi:.2f}, NDMI={metrics.ndmi:.2f}) and land cover fractions "
        f"{metrics.land_cover}."
    )
    estimated = (
        f"Estimated: relative biomass score is {metrics.biomass_score:.2f} "
        f"({metrics.biomass_category})."
    )
    inferred = (
        f"Inferred: ecological context aligns with {metrics.ecoregion} biome class "
        f"({metrics.biome})."
    )
    uncertain = (
        "Uncertain: species-level presence/absence cannot be confirmed from this "
        "imagery-only analysis."
    )
    return "\n".join([observed, estimated, inferred, uncertain])
