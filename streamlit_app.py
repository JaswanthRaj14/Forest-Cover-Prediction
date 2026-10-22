
import streamlit as st
import requests

st.set_page_config(
    page_title="Forest Cover Prediction",
    page_icon="🌲",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"

TERRAIN_FEATURES = [
    "Elevation",
    "Aspect",
    "Slope",
    "Horizontal_Distance_To_Hydrology",
    "Vertical_Distance_To_Hydrology",
    "Horizontal_Distance_To_Roadways",
    "Hillshade_9am",
    "Hillshade_Noon",
    "Hillshade_3pm",
    "Horizontal_Distance_To_Fire_Points",
]

WILDERNESS_FEATURES = [
    "Wilderness_Area1",
    "Wilderness_Area2",
    "Wilderness_Area3",
    "Wilderness_Area4",
]

SOIL_FEATURES = [
    "Soil_Type1", "Soil_Type2", "Soil_Type3", "Soil_Type4",
    "Soil_Type5", "Soil_Type6", "Soil_Type8", "Soil_Type9",
    "Soil_Type10", "Soil_Type11", "Soil_Type12", "Soil_Type13",
    "Soil_Type14", "Soil_Type16", "Soil_Type17", "Soil_Type18",
    "Soil_Type19", "Soil_Type20", "Soil_Type21", "Soil_Type22",
    "Soil_Type23", "Soil_Type24", "Soil_Type25", "Soil_Type26",
    "Soil_Type27", "Soil_Type28", "Soil_Type29", "Soil_Type30",
    "Soil_Type31", "Soil_Type32", "Soil_Type33", "Soil_Type34",
    "Soil_Type35", "Soil_Type36", "Soil_Type37", "Soil_Type38",
    "Soil_Type39", "Soil_Type40",
]

COVER_NAMES = {
    1: "Spruce/Fir",
    2: "Lodgepole Pine",
    3: "Ponderosa Pine",
    4: "Cottonwood/Willow",
    5: "Aspen",
    6: "Douglas-fir",
    7: "Krummholz",
}

st.title("🌲 Forest Cover Prediction")
st.write(
    "Predict one of seven forest cover types using "
    "terrain, wilderness, and soil information."
)

st.info(
    "Enter terrain measurements, select the applicable "
    "wilderness area, and select the soil type."
)

with st.form("prediction_form"):
    st.subheader("1. Terrain Features")

    features = {}

    terrain_columns = st.columns(2)

    for i, name in enumerate(TERRAIN_FEATURES):
        with terrain_columns[i % 2]:
            features[name] = st.number_input(
                name.replace("_", " "),
                value=0.0,
                step=1.0,
                key=name,
            )

    st.subheader("2. Wilderness Area")

    wilderness_choice = st.selectbox(
        "Select the wilderness area",
        options=WILDERNESS_FEATURES,
        format_func=lambda x: x.replace("_", " "),
    )

    for name in WILDERNESS_FEATURES:
        features[name] = int(name == wilderness_choice)

    st.subheader("3. Soil Type")

    soil_choice = st.selectbox(
        "Select the soil type",
        options=SOIL_FEATURES,
        format_func=lambda x: x.replace("_", " "),
    )

    for name in SOIL_FEATURES:
        features[name] = int(name == soil_choice)

    submitted = st.form_submit_button(
        "🌲 Predict Forest Cover",
        use_container_width=True,
    )

if submitted:
    payload = {
        "features": {
            name: float(value)
            for name, value in features.items()
        }
    }

    try:
        with st.spinner("Predicting forest cover..."):
            response = requests.post(
                API_URL,
                json=payload,
                timeout=30,
            )

        if response.status_code == 200:
            result = response.json()
            cover_type = result["predicted_cover_type"]
            cover_name = result.get(
                "predicted_cover_name",
                COVER_NAMES.get(cover_type, "Unknown"),
            )

            st.success("Prediction completed successfully!")
            st.metric("Predicted Cover Type", cover_type)
            st.subheader(f"🌲 {cover_name}")

        else:
            st.error(f"API error ({response.status_code})")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to FastAPI. "
            "Make sure app.py is running on port 8000."
        )

    except requests.exceptions.RequestException as exc:
        st.error(f"Request failed: {exc}")
