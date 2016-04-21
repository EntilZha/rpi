from django.db import models


class TemperatureReading(models.Model):
    recorded_time = models.DateTimeField('Temperature recorded time')
    temperature_c = models.FloatField()
    temperature_f = models.FloatField()
