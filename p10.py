import requests

response = requests.get(url="https://api.open-meteo.com/v1/forecast?latitude=24.8949&longitude=91.8687&timezone=Asia%2FDhaka&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
if response.status_code == 200:
    data = response.json()
    
    current = data ["current"]
    temperature = current["temperature_2m"]
    time = current["time"]
    wind_speed_10m = current["wind_speed_10m"]
    
    print("Sylhet Weather: ")
    print(f"Time: {time}")
    print (f"Temparature: {temperature} °C")
    print (f"WindSpeed : {wind_speed_10m} km/h")

else:
    print("Data is failed to fetch, Please try again later! ")
