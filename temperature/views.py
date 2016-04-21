from django.shortcuts import render
from temperature.models import TemperatureReading


def index(request):
    temperature_list = TemperatureReading.objects.order_by('-recorded_time')
    context = {'temperature_list': temperature_list}
    return render(request, 'temperature/index.html', context)
