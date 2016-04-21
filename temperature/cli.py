import subprocess
from datetime import datetime
from .models import TemperatureReading
import click


@click.group()
def main():
    pass


@main.command()
def record():
    raw_temp = subprocess.run(
        ['echo', '2016/04/21 07:04:12 Temperature 65.97F 18.88C'], stdout=subprocess.PIPE)
    tokens = raw_temp.stdout.strip().split()
    recorded_time = datetime.strftime(tokens[0] + ' ' + tokens[1], '%Y/%m/%d %I/%M/%s')
    temp_f = float(tokens[3].replace('F', ''))
    temp_c = float(tokens[4].replace('C', ''))
    reading = TemperatureReading(
        recorded_time=recorded_time, temperature_f=temp_f, temperature_c=temp_c)
    recording.save()
    with open('temp.log', 'a') as f:
        f.write(raw_temp.stdout)


if __name__ == '__main__':
    main()
