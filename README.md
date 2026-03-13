# Satellite Ecological Analysis Platform (MVP)

This repository implements an MVP architecture for a satellite ecological analysis platform using:

- **FastAPI** backend (`app/api`)
- **Streamlit** frontend (`app/web`)
- **Modular geospatial and interpretation services** (`app/api/services`)

## Implemented MVP capabilities

- AOI input via coordinates/place name (API and UI)
- Sentinel-2 processing stub hook (`gee_service.py`)
- NDVI/EVI/NDMI index pipeline
- Relative biomass scoring:

```text
BiomassScore = 0.45 * NDVI_norm + 0.35 * EVI_norm + 0.20 * NDMI_norm
```

- Biomass categories: Very Low / Low / Medium / High / Very High
- Basic land-cover heuristic classification
- Ecoregion + biome context inference stub
- AI-style interpretation text split into: **Observed / Estimated / Inferred / Uncertain**
- Report artifact export

## API endpoints

- `POST /analysis/run`
- `POST /analysis/upload-aoi`
- `GET /analysis/{id}`
- `GET /analysis/{id}/map`
- `GET /analysis/{id}/metrics`
- `GET /analysis/{id}/report`
- `GET /ecology/ecoregion`
- `GET /health`

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.api.main:app --reload
```

In another terminal:

```bash
streamlit run app/web/streamlit_app.py
```

## Run with Docker Compose

```bash
docker compose up --build
```

## Notes

This is a production-ready scaffold with deterministic placeholder geospatial logic. Integrate real Google Earth Engine authentication and analysis in `gee_service.py`, and add persistent storage layer backed by PostgreSQL/PostGIS for analysis records.
