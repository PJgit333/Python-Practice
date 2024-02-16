import requests

city = "Pune"
url = 'http://api.weatherapi.com/v1/current.json?key=5be4efdab4c44c09a6063729241302&q='+city+'&aqi=no'

response = requests.get(url)

weather_json = response.json()
temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Temperature of city", city, "is", temp)
print("today's weather is ",description)