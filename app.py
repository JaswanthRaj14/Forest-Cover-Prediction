import joblib
from fastapi import FastAPI
app = FastAPI(title="Forest Cover Predication API")
model = joblib.load("forest_cover_model.pkl")

import pandas as pd
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Dict

class PredictionRequest(BaseModel):
    features:Dict[str, float]

@app.get("/")
def home():
    return{"message": "Forest Cover Prediction API is running"}

@app.post("/predict")
def predict(request: PredictionRequest):
    expected_features = [ "Elevation", "Aspect", "Slope",
    "Horizontal_Distance_To_Hydrology",
    "Vertical_Distance_To_Hydrology",
    "Horizontal_Distance_To_Roadways",
    "Hillshade_9am", "Hillshade_Noon", "Hillshade_3pm",
    "Horizontal_Distance_To_Fire_Points",
    "Wilderness_Area1", "Wilderness_Area2",
    "Wilderness_Area3", "Wilderness_Area4",
    "Soil_Type1", "Soil_Type2", "Soil_Type3", "Soil_Type4",
    "Soil_Type5", "Soil_Type6", "Soil_Type8", "Soil_Type9",
    "Soil_Type10", "Soil_Type11", "Soil_Type12", "Soil_Type13",
    "Soil_Type14", "Soil_Type16", "Soil_Type17", "Soil_Type18",
    "Soil_Type19", "Soil_Type20", "Soil_Type21", "Soil_Type22",
    "Soil_Type23", "Soil_Type24", "Soil_Type25", "Soil_Type26",
    "Soil_Type27", "Soil_Type28", "Soil_Type29", "Soil_Type30",
    "Soil_Type31", "Soil_Type32", "Soil_Type33", "Soil_Type34",
    "Soil_Type35", "Soil_Type36", "Soil_Type37", "Soil_Type38",
    "Soil_Type39", "Soil_Type40"
]
    received_features = request.features
    print("Expected feature count:", len(expected_features))
    print("Received feature count:", len(received_features))    

    if set(received_features.keys()) != set(expected_features):
        raise HTTPException(status_code=400, detail="Provide exactly 52 features to Model.")

    input_data = pd.DataFrame(
                [[received_features[name] for name in expected_features]],
        columns=expected_features
    )

    prediction = int(model.predict(input_data)[0])

    cover_type_names = {
        1: "Spruce/Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood/Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    return {
        "predicted_cover_type": prediction,
        "predicted_cover_name": cover_type_names[prediction]
    }

