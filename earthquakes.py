import requests
from datetime import datetime

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"


response = requests.get(url, headers={'Accept':'application/json'}, params={
    'format':'geojson',
    'starttime':'2011-01-01',
    'endtime':'2021-01-01',
    'latitude':'43.6',
    'longitude':'39.73',
    'maxradiuskm':'300'
})

data = response.json()
number_of_earthquakes = data['metadata']['count']
x = 0

for i in data['features']:
    timestamp = data['features'][x]['properties']['time']/1000
    time = datetime.fromtimestamp(timestamp)
    print(data['features'][x]['properties']['place'])
    print(time.strftime('%H:%M:%S %Y-%m-%d'))
    print('Magnitude:', data['features'][x]['properties']['mag'])
    print(' ')
    x += 1
print(number_of_earthquakes)
