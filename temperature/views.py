from django.shortcuts import render
from temperature.models import TemperatureReading


def index(request):
    temperature_list = TemperatureReading.objects.order_by('-id')
    context = {'temperature_list': temperature_list, 'current_temp': temperature_list[0]}
    return render(request, 'temperature/index.html', context)
