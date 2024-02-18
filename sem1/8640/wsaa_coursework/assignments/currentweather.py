import requests

def deg_to_wind_dir(deg):
    dir = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round((deg % 360) / (360. / len(dir)))

    return dir[index % len(dir)]

def main():
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m,wind_direction_10m"

    page = requests.get(url)
    data = page.json()

    temperature = data['current']['temperature_2m']
    wind_direction_deg = data['current']['wind_direction_10m']
    wind_direction = deg_to_wind_dir(wind_direction_deg)

    print("Current temperature is " + str(temperature) + " degrees Celsius.")
    print("Current wind direction is " + str(wind_direction) + " or " + str(wind_direction_deg) + " degrees.")

if __name__ == '__main__':
    main()