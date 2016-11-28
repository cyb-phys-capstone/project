# Prototype to demonstrate retrieval of NREL solar data
# Python 3.5.2

import json
import requests

class NREL(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

url = 'http://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=DEMO_KEY&lat=33&lon=-111'
response = requests.get(url)

nrel = NREL(response.text)

outputs = nrel.outputs
tilt = outputs['avg_lat_tilt']

dni = outputs['avg_dni']

ghi = outputs['avg_ghi']

print("=====Average Tilt at Latitude=====")
print("Annual: " + str(tilt['annual']))
print("Monthly")
for key in tilt['monthly'].keys():
    print(key + ": " + str(tilt['monthly'][key]))

print("=====Average Direct Normal Irradiance=====")
print("Annual: " + str(dni['annual']))
print("Monthly")
for key in dni['monthly'].keys():
    print(key + ": " + str(dni['monthly'][key]))
    
print("=====Average Global Horizontal Irradiance=====")
print("Annual: " + str(ghi['annual']))
print("Monthly")
for key in ghi['monthly'].keys():
    print(key + ": " + str(ghi['monthly'][key]))
