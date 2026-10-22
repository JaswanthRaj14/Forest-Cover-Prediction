
import streamlit as st
import pandas as pd
import joblib
import gdown
from pathlib import Path

# --------------------------------------------------
# 1. Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Forest Cover Prediction",
    page_icon="🌲",
    layout="wide",
)

st.title("🌲 Forest Cover Prediction")
st.write(
    "Predict one of seven forest cover types using "
    "terrain, wilderness, and soil information."
)

st.info(
    "Enter the terrain measurements and select the "
    "wilderness area and soil type to make a prediction."
)

# --------------------------------------------------
# 2. Model Configuration
# --------------------------------------------------

MODEL_PATH = Path(__file__).resolve().parent / "forest_cover_model.pkl"
DRIVE_FILE_ID = "15swC0zRpHywYzCGOM0cIzrNUcv1Ir2nH"

COVER_NAMES = {
    1: "Spruce/Fir",
    2: "Lodgepole Pine",
    3: "Ponderosa Pine",
    4: "Cottonwood/Willow",
    5: "Aspen",
    6: "Douglas-fir",
    7: "Krummholz",
}


@st.cache_resource
def load_model():
    """Download the model if needed, then load it."""

    if not MODEL_PATH.exists():
        downloaded_file = gdown.download(
            id=DRIVE_FILE_ID,
            output=str(MODEL_PATH),
            quiet=False,
        )

        if not downloaded_file or not MODEL_PATH.exists():
            raise RuntimeError(
                "Model download failed. Check that the "
                "Google Drive file is accessible to anyone "
                "with the link."
            )

    return joblib.load(MODEL_PATH)


# --------------------------------------------------
# 3. Feature Definitions
# --------------------------------------------------

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

# These are the exact 52 features used by the trained model.
MODEL_FEATURES = TERRAIN_FEATURES + WILDERNESS_FEATURES + SOIL_FEATURES


# --------------------------------------------------
# 4. Input Form
# --------------------------------------------------

with st.form("prediction_form"):

    st.subheader("1. Terrain Features")

    features = {}
    terrain_columns = st.columns(2)

    for i, name in enumerate(TERRAIN_FEATURES):
        with terrain_columns[i % 2]:
            features[name] = st.number_input(
                name.replace("_", " "),
                min_value=0.0,
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


# --------------------------------------------------
# 5. Make Prediction
# --------------------------------------------------

if submitted:

    try:
        # Ensure the input order matches model training.
        input_df = pd.DataFrame(
            [[features[name] for name in MODEL_FEATURES]],
            columns=MODEL_FEATURES,
        )

        with st.spinner(
            "Loading the model and predicting forest cover..."
        ):
            model = load_model()
            prediction = int(model.predict(input_df)[0])

        cover_name = COVER_NAMES.get(
            prediction,
            "Unknown cover type",
        )

        st.success("Prediction completed successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Predicted Cover Type",
                prediction,
            )

        with col2:
            st.metric(
                "Predicted Forest",
                cover_name,
            )

        st.subheader(f"🌲 {cover_name}")

        st.caption(
            "This result is a machine-learning prediction, "
            "not a guarantee of the actual forest cover."
        )

    except Exception as exc:
        st.error(
            "The prediction could not be completed. "
            "Check the model download, dependencies, and "
            "model compatibility."
        )
        st.exception(exc)
