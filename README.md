# AQI Predictor

AQI Predictor is a Django-based web application that estimates the Air Quality Index (AQI) from pollutant concentration values. The project combines a trained machine learning model with a simple web interface so users can enter pollutant readings and receive an AQI score and category.

## Project overview

This application is designed to help users quickly estimate air quality using common pollution metrics such as PM2.5, PM10, NO2, SO2, CO, and O3. It uses a Random Forest model for prediction and stores each submitted prediction in a local SQLite database.

The project is organized as a Django application with:

- A web form for entering pollutant values
- A result page showing the predicted AQI and category
- A home and about page for general context
- A trained model and scaler loaded at runtime from serialized files

## Key features

- Predict AQI from six key pollutant inputs
- Classify AQI into categories such as Good, Moderate, Unhealthy, Very Unhealthy, and Hazardous
- Save prediction records in SQLite
- Load a pre-trained machine learning model from serialized `.pkl` files
- Fall back to a simple mock AQI calculation if the model files are unavailable
- Use a clean frontend built with HTML, CSS, and JavaScript

## Technologies used

- Python
- Django 4.2.7
- NumPy
- Pandas
- scikit-learn
- Joblib
- SQLite
- HTML, CSS, JavaScript

## Project structure

```text
AQI_project/
├── .git/
├── .gitignore
├── README.md
├── aqi_project/
│   ├── aqi_app/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── aqi_project/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── prediction.html
│   │   └── result.html
│   ├── .gitignore
│   ├── Aqi-project.ipynb
│   ├── AQIipynb
│   ├── aqi_scaler.pkl
│   ├── best_aqi_model.pkl
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
└──
```

## Main entry points

- Application entry point: `aqi_project/manage.py`
- Django project settings: `aqi_project/aqi_project/settings.py`
- App routes: `aqi_project/aqi_app/urls.py`
- Predictive logic: `aqi_project/aqi_app/views.py`
- ML model files: `aqi_project/best_aqi_model.pkl` and `aqi_project/aqi_scaler.pkl`

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.10 or newer
- pip
- A virtual environment tool such as `venv`

## Installation and setup

From the repository root, create and activate a virtual environment, then install dependencies:

```bash
cd aqi_project
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

## Environment configuration

This repository does not contain a custom `.env` file or dedicated environment-variable-based configuration for local development. The project currently uses the default Django development settings and SQLite database configuration defined in `aqi_project/settings.py`.

If you deploy this project outside local development, it is recommended to move the Django secret key and database settings to environment variables and use a production-safe configuration.

## Running the project locally

Apply database migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Then open the app in your browser:

```text
http://127.0.0.1:8000/
```

## How the application works

1. The user opens the prediction page.
2. They enter pollutant values such as PM2.5, PM10, NO2, SO2, CO, and O3.
3. The application validates the inputs and prepares them for the ML model.
4. The scaler transforms the values and the model predicts an AQI score.
5. The app assigns an AQI category and displays the result.
6. The prediction is saved to the SQLite database.

If the serialized model files are missing or cannot be loaded, the app falls back to a simple weighted calculation for demonstration purposes.

## Usage instructions

- Open the home page to learn about the project.
- Click the "Get Prediction" button from the home page.
- Enter pollutant concentration values.
- Submit the form to view the AQI result.
- Use the "Make Another Prediction" button to return to the prediction page.


## Notebook and model files

The repository includes a notebook named `Aqi-project.ipynb` and a notebook-like folder named `AQIipynb`, which appear to be related to data preprocessing and model experimentation. The trained model files used by the web app are:

- `aqi_project/best_aqi_model.pkl`
- `aqi_project/aqi_scaler.pkl`

## Future improvements

Potential improvements for this project include:

- Adding a more robust production-ready configuration for environment variables and deployment
- Improving model validation and tracking metrics
- Supporting user authentication and prediction history dashboards
- Adding API endpoints for integration with external applications
- Expanding tests for forms, views, and prediction logic

## Contributing

Contributions are welcome. If you want to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Validate the relevant behavior locally.
5. Open a pull request with a clear description of the changes.

Please keep changes focused and avoid modifying unrelated files.

## License


## Notes

This project is a local development prototype for AQI prediction and does not currently include deployment configuration or a production-ready infrastructure setup.
