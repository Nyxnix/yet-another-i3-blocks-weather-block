# i3 block that uses accuweather api

import json
import os
import math
import urllib.request

# Check if file exists and init if not
def where_json(file_name):
    return os.path.exists(file_name)

if where_json('config.json'):
    pass
else:
    data = {  
        'apikey': "Put key here",
        'tempUnit': "F",
        'cityName': "New York"
    }
    with open('config.json', 'w') as config_file:  
        json.dump(data, config_file)

# Read the config file and request data from api
with open('config.json', 'r') as f:
    config = json.load(f)
    api_key = config.get('apikey')
    temp_unit = config.get('tempUnit')
    location = urllib.parse.quote(config.get('cityName'))
weather_data = urllib.request.urlopen(f"http://dataservice.accuweather.com/locations/v1/search?q={location}&apikey={api_key}").read()
weather_data = json.loads(weather_data.decode('utf-8'))

# parse data to get location key for next calls
location_key = weather_data[0].get('Key')
current_weather = urllib.request.urlopen(f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}").read()
current_weather = json.loads(current_weather.decode('utf-8'))

# prep data
weather_text = current_weather[0].get('WeatherText')
temperature = current_weather[0].get('Temperature')

if temp_unit == "F":
    temperature = temperature.get('Imperial')
    value = temperature.get('Value')
    unit = temperature.get('Unit')
    text = f"{weather_text} // {value}{unit}"
    print(text)
elif temp_unit == "C":
    temperature = temperature.get('Metric')
    print(temperature)
else:
    raise Exception("Invalid tempUnit. Use 'F' or 'C'.")
