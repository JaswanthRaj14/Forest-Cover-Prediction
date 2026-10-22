# Forest-Cover-Prediction
Multiclass machine learning project for predicting forest cover types using terrain and environmental features, with a FastAPI backend and Streamlit interface.  

# 🌲 Forest Cover Prediction

A machine learning web application that predicts forest cover types from cartographic, terrain, wilderness-area, and soil information using an **Extra Trees Classifier**.

<p align="center">
  <a href="https://forest-cover-prediction-dm3gypgxmgmbpwnyeozxnv.streamlit.app/"><strong>🚀 Live Demo</strong></a>
  &nbsp; | &nbsp;
  <a href="https://github.com/JaswanthRaj14/Forest-Cover-Prediction"><strong>💻 GitHub Repository</strong></a>
</p>

---

## 📌 Project Overview

Forest cover classification helps identify the vegetation type associated with a particular area using environmental and geographical characteristics.

This project develops a multiclass machine learning model that predicts one of **seven forest cover types** using 52 input features. The trained model is integrated into a Streamlit web application, allowing users to enter terrain measurements, select a wilderness area and soil type, and receive a prediction.

The application is publicly deployed, and the trained model is stored separately on Google Drive rather than committed to GitHub because of its file size.

## 🎯 Objectives

- Develop a multiclass classification model for forest cover prediction.
- Explore terrain, hydrological, soil, and wilderness-area features.
- Evaluate model performance using accuracy and macro F1-score.
- Build an interactive web interface for generating predictions.
- Deploy the application for public access.
- Manage source code and project documentation using Git and GitHub.

## 🚀 Live Application

**Try the application:** [Forest Cover Prediction — Streamlit](https://forest-cover-prediction-dm3gypgxmgmbpwnyeozxnv.streamlit.app/)

Users can enter terrain measurements, select a wilderness area and soil type, and generate a predicted forest cover category.

## 📊 Model Performance

| Metric | Result |
|---|---:|
| Algorithm | Extra Trees Classifier |
| Classification type | Multiclass classification |
| Number of classes | 7 |
| Input features | 52 |
| Number of trees | 100 |
| Holdout accuracy | 86.08% |
| Macro F1-score | 0.8591 |

**Evaluation note:** These results were obtained on a holdout split from the same underlying dataset used during project development. They should not be interpreted as performance on a fully independent external dataset.

## 🌳 Forest Cover Classes

The model predicts one of the following classes:

| Class | Forest Cover Type |
|---:|---|
| 1 | Spruce/Fir |
| 2 | Lodgepole Pine |
| 3 | Ponderosa Pine |
| 4 | Cottonwood/Willow |
| 5 | Aspen |
| 6 | Douglas-fir |
| 7 | Krummholz |

## 🧩 Input Features

The application uses 52 features organized into three groups.

### 1. Terrain Features — 10

- Elevation
- Aspect
- Slope
- Horizontal Distance to Hydrology
- Vertical Distance to Hydrology
- Horizontal Distance to Roadways
- Hillshade at 9 AM
- Hillshade at Noon
- Hillshade at 3 PM
- Horizontal Distance to Fire Points

### 2. Wilderness Area Features — 4

Binary indicators representing the four wilderness areas.

### 3. Soil Type Features — 38

Binary indicators representing the soil categories retained in the model's feature set.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming language | Python |
| Data analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine learning | Scikit-learn |
| Model serialization | Joblib |
| Web application | Streamlit |
| Model storage | Google Drive |
| Version control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## ⚙️ How It Works

1. **Data preparation:** Examine the dataset and prepare the features required for classification.
2. **Feature selection:** Retain the 52 features used by the trained model.
3. **Model training:** Train an Extra Trees Classifier with 100 trees.
4. **Evaluation:** Assess the model using a holdout split and report accuracy and macro F1-score.
5. **Model serialization:** Save the trained model using Joblib.
6. **Application development:** Build a Streamlit interface for collecting input values and displaying predictions.
7. **Model loading:** Download the model from Google Drive when it is not available locally, then cache the loaded model during the running application session.
8. **Deployment:** Publish the application through Streamlit Community Cloud.

## 🖥️ Run the Project Locally

### Prerequisites

- Python compatible with the pinned Scikit-learn version
- Git
- Internet access for downloading the model from Google Drive

### 1. Clone the repository

```bash
git clone https://github.com/JaswanthRaj14/Forest-Cover-Prediction.git
cd Forest-Cover-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python -m streamlit run streamlit_app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser.

**Model download:** The application downloads `forest_cover_model.pkl` from Google Drive if the file is not already present in the project directory. The Google Drive file must be accessible to viewers with the link. The first download may take time because the model is approximately 123 MB.

**Important:** Do not commit the model file to GitHub. It is excluded through `.gitignore`.

## 📁 Project Structure

```text
Forest-Cover-Prediction/
├── ForestCover.ipynb
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

The trained model, `forest_cover_model.pkl`, is downloaded separately at runtime and is not included in the Git repository.

- `ForestCover.ipynb` — data exploration, model development, and evaluation.
- `streamlit_app.py` — interactive prediction interface and model loading.
- `app.py` — FastAPI prediction backend retained in the repository.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local data, environment files, and the large model artifact.

The currently deployed Streamlit application makes predictions directly and does not require a separately running local FastAPI server.


## 📚 Dataset Attribution

This project uses the **Covertype (Forest Cover Type)** dataset associated with the UCI Machine Learning Repository.

The dataset concerns forest cover types in the Roosevelt National Forest region of northern Colorado and includes cartographic variables describing terrain, hydrology, roadways, wilderness areas, and soil types. The source data is associated with work by the U.S. Forest Service and U.S. Geological Survey.

- **Dataset:** [Covertype — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/31/covertype)

This repository documents a machine learning application developed using the dataset. Refer to the original dataset source for its official citation and applicable usage terms.

## 🔮 Future Improvements

- Add visualizations explaining important model features.
- Improve input validation and user guidance.
- Provide more detailed prediction explanations.
- Evaluate generalization using a genuinely independent dataset.
- Add automated deployment checks and model download error handling.
- Improve loading feedback and deployment reliability.

## 👨‍💻 Author

**Jaswanth Raj**

- GitHub: [@JaswanthRaj14](https://github.com/JaswanthRaj14)
- Project Repository: [Forest Cover Prediction](https://github.com/JaswanthRaj14/Forest-Cover-Prediction)
- Live Application: [Open the Demo](https://forest-cover-prediction-dm3gypgxmgmbpwnyeozxnv.streamlit.app/)

---

*Built as a machine learning portfolio project to explore multiclass classification, environmental data, model evaluation, and public application deployment.*
