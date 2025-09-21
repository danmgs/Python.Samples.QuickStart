import requests

API_KEY = "ta_clef_api"
city = "Paris"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

resp = requests.get(url).json()
print(f"Météo à {city}: {resp['main']['temp']}°C, {resp['weather'][0]['description']}")
