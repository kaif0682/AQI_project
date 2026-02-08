from django.db import models

class AQIPrediction(models.Model):
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    no2 = models.FloatField()
    so2 = models.FloatField()
    co = models.FloatField()
    o3 = models.FloatField()
    predicted_aqi = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"AQI Prediction {self.id}"