from django import forms

class AQIPredictionForm(forms.Form):
    pm25 = forms.FloatField(
        label="PM2.5 (μg/m³)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )
    pm10 = forms.FloatField(
        label="PM10 (μg/m³)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )
    no2 = forms.FloatField(
        label="NO2 (ppb)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )
    so2 = forms.FloatField(
        label="SO2 (ppb)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )
    co = forms.FloatField(
        label="CO (ppm)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    o3 = forms.FloatField(
        label="O3 (ppb)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )