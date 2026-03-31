import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            print("Weather:", data["weather"][0]["description"])

        elif response.status_code == 429:
            print("⚠️ Too many requests. Please try again later.")

        else:
            print(f"❌ Error: {response.status_code}")

    except Exception as e:
        print("⚠️ Network error:", str(e))


# NOTE:
# We do NOT log user location data (city names) to protect user privacy.
# According to GDPR, location data is personal data and should not be logged.

city = input("Enter city name: ")
get_weather(city) 
