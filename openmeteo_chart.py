# open-meteo chart
import asciichartpy
import requests

r = requests.get(
    f'https://api.open-meteo.com/v1/forecast?latitude={-53.79}&longitude={-67.69}&hourly=temperature_2m')
u_data = r.json()

xl = u_data['hourly']
x = xl['temperature_2m']
out_l = asciichartpy.plot(x)

# Print to the text file


def makefile(filename=''):
    file = open(filename, 'w')
    print(out_l, file=file)
    file.close()
    return filename


makefile('tlog.txt')
