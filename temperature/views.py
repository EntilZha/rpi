from django.http import HttpResponse
from temperature.models import TemperatureReading


def index(request):
    temps = TemperatureReading.objects.order_by('-recorded_time')
    output = '\n'.join([str((t.recorded_time, t.temperature_f, t.temperature_c)) for t in temps])
    return HttpResponse(output)
