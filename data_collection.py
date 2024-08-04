import requests
import time
import csv
import logging
import os

# Fetch the API key from the environment variable
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")
print(f"API_KEY: {API_KEY}")

logging.basicConfig(filename='/Users/admin/logs/data_collection.log', level=logging.DEBUG)
logging.debug(f"API_KEY: {API_KEY}")

def fetch_weather_data(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        logging.debug(f"Request URL: {url}")
        response = requests.get(url, timeout=10)
        logging.debug(f"Response Status Code: {response.status_code}")
        if response.status_code == 401:
            logging.error("Unauthorized request. Check the API key.")
            return None
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data for {city}: {e}")
        return None

def main():
    cities = ['London'] * 5  # Reduced for testing
    with open('/Users/admin/output_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['city', 'temperature', 'weather', 'humidity', 'wind_speed', 'pressure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for city in cities:
            logging.info(f"Fetching weather data for {city}")
            data = fetch_weather_data(city)
            if data:
                logging.info(f"Successfully fetched data for {city}")
                writer.writerow({
                    'city': city,
                    'temperature': data['main']['temp'],
                    'weather': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'pressure': data['main']['pressure']
                })
            time.sleep(10)  # Increased wait for testing

if __name__ == "__main__":
    logging.info("Starting data collection")
    main()
    logging.info("Data collection completed")

