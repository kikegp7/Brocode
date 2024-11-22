import requests
from weather_key import key

city_name = input("Nombre de ciudad: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}"
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    weather_id = weather_data["weather"]
    print(weather_data["main"].get("tempCelsius"))
    print(weather_id)
else:
    print(f"Failed to retrieve data {response.status_code}")


