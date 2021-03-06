import subprocess
from datetime import datetime
from django.utils.timezone import make_aware, get_default_timezone
from django.core.management.base import BaseCommand
from temperature.models import TemperatureReading


class Command(BaseCommand):
    def handle(self, *args, **options):
        raw_temp = subprocess.run(
            ['/usr/local/bin/pcsensor'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        tokens = raw_temp.strip().split()
        zone = get_default_timezone()
        datetime_str = '{0} {1}'.format(tokens[0], tokens[1])
        recorded_time = make_aware(
            datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S'), timezone=zone)
        temp_f = float(tokens[3].replace('F', ''))
        temp_c = float(tokens[4].replace('C', ''))
        reading = TemperatureReading(
            recorded_time=recorded_time, temperature_f=temp_f, temperature_c=temp_c)
        reading.save()
        with open('temp.log', 'a') as f:
            f.write(raw_temp)
        self.stdout.write(self.style.SUCCESS('Successfully recorded temperature'))
