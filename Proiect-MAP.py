import os
import dotenv
import requests

dotenv.load_dotenv()

api_key = os.getenv("API_KEY")
oras = input("Introduceti numele orasului: ").strip()

url = "https://api.openweathermap.org/data/2.5/weather"
parametri = {
    "q": oras,
    "appid": api_key,
    "units": "metric",
}

with requests.get(url, params=parametri) as raspuns:
    raspuns.raise_for_status()
    raspunsweather = raspuns.json()

stareavremi = raspunsweather["weather"][0]["main"]
temperature = raspunsweather["main"]["temp"]
viteza_vantului = raspunsweather["wind"]["speed"]
print(f"Starea vremii: {stareavremi}")
print(f"Temperatura: {temperature}")
print(f"Viteza vantului: {viteza_vantului}")