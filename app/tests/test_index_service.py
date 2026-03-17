from app.api.services.index_service import VegetationIndices, biomass_category, biomass_score


def test_biomass_score_range() -> None:
    score = biomass_score(VegetationIndices(ndvi=0.6, evi=0.5, ndmi=0.4))
    assert 0 <= score <= 1


def test_biomass_category() -> None:
    assert biomass_category(0.1) == "Very Low"
    assert biomass_category(0.35) == "Low"
    assert biomass_category(0.55) == "Medium"
    assert biomass_category(0.75) == "High"
    assert biomass_category(0.95) == "Very High"
