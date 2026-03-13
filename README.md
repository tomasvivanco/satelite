# Satellite Ecological Analysis Platform (MVP)

This repository implements an MVP architecture for a satellite ecological analysis platform using:

- **FastAPI** backend (`app/api`)
- **Streamlit** frontend (`app/web`)
- **GitHub Pages static frontend** (`docs/`) for simple public hosting
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

## Make the app usable on GitHub Pages

A static web UI is provided in `docs/index.html` and is deployed with GitHub Actions (`.github/workflows/deploy-pages.yml`).

### 1) Enable Pages in your repo

- Go to **Settings → Pages**.
- Source should be **GitHub Actions**.

### 2) Deploy backend API somewhere public

GitHub Pages only hosts static files, so the FastAPI backend must run elsewhere (Render, Fly.io, Railway, GCP, Azure, VPS, etc.).

Example environment variable for CORS (if you want to lock it down):

```bash
CORS_ORIGINS=https://<your-user>.github.io
```

Current default allows all origins for easier MVP usage.

### 3) Use the Pages UI

After deployment, open:

- `https://<your-user>.github.io/<repo>/`

In the UI:
- Set **API Base URL** to your deployed backend (e.g. `https://your-api.example.com`)
- Run analysis directly from the browser

You can also prefill the API URL via query string:

- `https://<your-user>.github.io/<repo>/?apiBase=https://your-api.example.com`

## How to test the app

### Option A: Test with Docker Compose (recommended)

```bash
docker compose up --build
```

This starts:
- API at `http://localhost:8000`
- Streamlit web app at `http://localhost:8501`
- PostGIS at `localhost:5432`

Then run an end-to-end smoke test from another terminal:

```bash
bash scripts/smoke_test.sh
```

You can also pass a custom API base URL:

```bash
bash scripts/smoke_test.sh http://localhost:8000
```

### Option B: Test locally without Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.api.main:app --reload
```

In another terminal:

```bash
source .venv/bin/activate
streamlit run app/web/streamlit_app.py
```

In a third terminal, run smoke checks:

```bash
bash scripts/smoke_test.sh
```

## Run automated tests

```bash
python -m pytest -q app/tests/test_index_service.py
python -m pytest -q app/tests/test_api.py
```

If dependencies are unavailable in your environment, use Docker Compose testing path above.

## Notes

This is a production-ready scaffold with deterministic placeholder geospatial logic. Integrate real Google Earth Engine authentication and analysis in `gee_service.py`, and add persistent storage layer backed by PostgreSQL/PostGIS for analysis records.
