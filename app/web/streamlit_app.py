import requests
import streamlit as st

API_BASE = st.secrets.get("api_base", "http://localhost:8000")

st.set_page_config(page_title="Satellite Ecological Analysis", layout="wide")
st.title("Satellite Ecological Analysis Platform")

with st.sidebar:
    st.header("Analysis Input")
    input_type = st.selectbox("Input type", ["coordinates", "place_name"])

    latitude = st.number_input("Latitude", value=0.0, format="%.6f")
    longitude = st.number_input("Longitude", value=0.0, format="%.6f")
    place_name = st.text_input("Place name")
    run = st.button("Run Analysis")

if run:
    payload = {
        "input_type": input_type,
        "latitude": latitude,
        "longitude": longitude,
        "location_query": place_name,
    }
    result = requests.post(f"{API_BASE}/analysis/run", json=payload, timeout=60)
    if result.ok:
        data = result.json()
        st.success(f"Analysis complete: {data['analysis_id']}")
        c1, c2, c3, c4 = st.columns(4)
        metrics = data["metrics"]
        c1.metric("NDVI", f"{metrics['ndvi']:.2f}")
        c2.metric("EVI", f"{metrics['evi']:.2f}")
        c3.metric("NDMI", f"{metrics['ndmi']:.2f}")
        c4.metric("Biomass", f"{metrics['biomass_score']:.2f} ({metrics['biomass_category']})")

        tabs = st.tabs(["Map", "Land Cover", "Interpretation"])
        with tabs[0]:
            st.info("Map rendering placeholder for Sentinel-2 composites and index overlays.")
        with tabs[1]:
            st.json(metrics["land_cover"])
        with tabs[2]:
            st.markdown(data["interpretation"])
    else:
        st.error(f"Analysis failed: {result.text}")
