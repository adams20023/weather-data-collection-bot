import requests
import os
import csv
import logging

# Configure logging
logging.basicConfig(filename='/Users/admin/logs/data_collection.log', level=logging.DEBUG)

API_KEY = os.getenv('API_KEY')
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

def fetch_weather_data():
    logging.info(f"Fetching weather data for {CITY}")
    try:
        response = requests.get(URL)
        logging.debug(f"Response Status Code: {response.status_code}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        logging.error(f"Error fetching data for {CITY}: {err}")
        return None

def write_data_to_csv(data, filename='/Users/admin/output_data.csv'):
    if data:
        logging.info(f"Writing data to {filename}")
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            main = data['main']
            writer.writerow({
                'temp': main['temp'],
                'feels_like': main['feels_like'],
                'temp_min': main['temp_min'],
                'temp_max': main['temp_max'],
                'pressure': main['pressure'],
                'humidity': main['humidity']
            })
        logging.info(f"Data successfully written to {filename}")
    else:
        logging.warning(f"No data to write to {filename}")

def main():
    data = fetch_weather_data()
    write_data_to_csv(data)
    print("Data collection complete")

if __name__ == "__main__":
    main()

