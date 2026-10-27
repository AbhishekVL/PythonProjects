import requests

def get_weather(city):
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
    data = response.json()

    if "results" not in data:
        print("City not found!")
        return

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m"
        f"&timezone=auto"
    )

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    print("City:", city)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Local Time:", weather_data["current"]["time"])
    print("Temperature:", weather_data["current"]["temperature_2m"], "°C")
    print("Humidity:", weather_data["current"]["relative_humidity_2m"], "%")

    return weather_data

get_weather("bagalkot")