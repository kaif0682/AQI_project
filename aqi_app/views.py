# import joblib
# import numpy as np
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .forms import AQIPredictionForm
# from .models import AQIPrediction

# # Load the pre-trained model and scaler
# try:
#     model = joblib.load("best_aqi_model.pkl")
#     scaler = joblib.load("aqi_scaler.pkl")
# except:
#     model = None
#     scaler = None

# def home(request):
#     return render(request, 'home.html')

# def prediction(request):
#     if request.method == 'POST':
#         form = AQIPredictionForm(request.POST)
#         if form.is_valid():
#             # Extract form data
#             pm25 = form.cleaned_data['pm25']
#             pm10 = form.cleaned_data['pm10']
#             no2 = form.cleaned_data['no2']
#             so2 = form.cleaned_data['so2']
#             co = form.cleaned_data['co']
#             o3 = form.cleaned_data['o3']
            
#             # Prepare data for prediction
#             input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
            
#             # Scale the input data
#             if scaler:
#                 input_data_scaled = scaler.transform(input_data)
#             else:
#                 input_data_scaled = input_data
            
#             # Make prediction
#             if model:
#                 predicted_aqi = model.predict(input_data_scaled)[0]
#             else:
#                 # Mock prediction for demo purposes
#                 predicted_aqi = (pm25 * 0.3 + pm10 * 0.2 + no2 * 0.15 + 
#                                 so2 * 0.15 + co * 0.1 + o3 * 0.1) * 10
            
#             # Determine AQI category
#             category = get_aqi_category(predicted_aqi)
            
#             # Save prediction to database
#             prediction_record = AQIPrediction(
#                 pm25=pm25, pm10=pm10, no2=no2, so2=so2, co=co, o3=o3,
#                 predicted_aqi=predicted_aqi, category=category
#             )
#             prediction_record.save()
            
#             # Redirect to result page
#             return render(request, 'result.html', {
#                 'prediction': predicted_aqi,
#                 'category': category,
#                 'input_data': {
#                     'pm25': pm25,
#                     'pm10': pm10,
#                     'no2': no2,
#                     'so2': so2,
#                     'co': co,
#                     'o3': o3
#                 }
#             })
#     else:
#         form = AQIPredictionForm()
    
#     return render(request, 'prediction.html', {'form': form})

# def result(request):
#     # This view is called from the prediction view with context
#     # If accessed directly, redirect to prediction page
#     return redirect('prediction')

# def about(request):
#     return render(request, 'about.html')

# def get_aqi_category(aqi_value):
#     if aqi_value <= 50:
#         return "Good"
#     elif aqi_value <= 100:
#         return "Moderate"
#     elif aqi_value <= 150:
#         return "Unhealthy for Sensitive Groups"
#     elif aqi_value <= 200:
#         return "Unhealthy"
#     elif aqi_value <= 300:
#         return "Very Unhealthy"
#     else:
#         return "Hazardous"

import joblib
import numpy as np
import os
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AQIPredictionForm
from .models import AQIPrediction

# Get the base directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the pre-trained model and scaler
try:
    model_path = os.path.join(BASE_DIR, "best_aqi_model.pkl")
    scaler_path = os.path.join(BASE_DIR, "aqi_scaler.pkl")
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    model_loaded = True
    print("Model and scaler loaded successfully!")
except Exception as e:
    model = None
    scaler = None
    model_loaded = False
    print(f"Error loading model: {e}")
    print("Using mock predictions for demonstration")

def home(request):
    context = {
        'model_loaded': model_loaded
    }
    return render(request, 'home.html', context)

def prediction(request):
    if request.method == 'POST':
        form = AQIPredictionForm(request.POST)
        if form.is_valid():
            # Extract form data
            pm25 = form.cleaned_data['pm25']
            pm10 = form.cleaned_data['pm10']
            no2 = form.cleaned_data['no2']
            so2 = form.cleaned_data['so2']
            co = form.cleaned_data['co']
            o3 = form.cleaned_data['o3']
            
            # Prepare data for prediction
            input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
            
            # Make prediction
            if model_loaded and model is not None and scaler is not None:
                try:
                    # Scale the input data
                    input_data_scaled = scaler.transform(input_data)
                    predicted_aqi = model.predict(input_data_scaled)[0]
                    prediction_method = "Random Forest Model"
                except Exception as e:
                    print(f"Prediction error: {e}")
                    predicted_aqi = calculate_mock_aqi(pm25, pm10, no2, so2, co, o3)
                    prediction_method = "Mock Calculation (Fallback)"
            else:
                predicted_aqi = calculate_mock_aqi(pm25, pm10, no2, so2, co, o3)
                prediction_method = "Mock Calculation"
            
            # Determine AQI category
            category = get_aqi_category(predicted_aqi)
            
            # Save prediction to database
            prediction_record = AQIPrediction(
                pm25=pm25, pm10=pm10, no2=no2, so2=so2, co=co, o3=o3,
                predicted_aqi=predicted_aqi, category=category
            )
            prediction_record.save()
            
            # Redirect to result page
            return render(request, 'result.html', {
                'prediction': predicted_aqi,
                'category': category,
                'input_data': {
                    'pm25': pm25,
                    'pm10': pm10,
                    'no2': no2,
                    'so2': so2,
                    'co': co,
                    'o3': o3
                },
                'prediction_method': prediction_method,
                'model_loaded': model_loaded
            })
    else:
        form = AQIPredictionForm()
    
    context = {
        'form': form,
        'model_loaded': model_loaded
    }
    return render(request, 'prediction.html', context)

def result(request):
    # This view is called from the prediction view with context
    # If accessed directly, redirect to prediction page
    return redirect('prediction')

def about(request):
    context = {
        'model_loaded': model_loaded
    }
    return render(request, 'about.html', context)

def get_aqi_category(aqi_value):
    if aqi_value <= 50:
        return "Good"
    elif aqi_value <= 100:
        return "Moderate"
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi_value <= 200:
        return "Unhealthy"
    elif aqi_value <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def calculate_mock_aqi(pm25, pm10, no2, so2, co, o3):
    """Fallback calculation if model fails to load"""
    # Simple weighted average for demonstration
    return (pm25 * 0.3 + pm10 * 0.2 + no2 * 0.15 + so2 * 0.15 + co * 0.1 + o3 * 0.1) * 10