import requests 


def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)
    data = response.json()
    

    if 'results' not in data:
        return None,None
    
    first = data["results"][0]
    return first['latitude'],first['longitude']

def get_weather(lat,lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    return response.json()

def main():
    city = input("Enter a city name:")

    lat,lon = get_coordinates(city)

    if lat is None:
        return "City Not Found"
    
    weather = get_weather(lat,lon)
    current = weather['current_weather']

    print (f"\nWeather in {city}")
    print(f"Temperature: {(current['temperature'] * 1.8) + 32} °F")
    print(f"Windspeed: {current['windspeed']} km/h")

if __name__ == "__main__":
    main()
