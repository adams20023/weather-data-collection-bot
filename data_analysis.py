import pandas as pd
import logging

logging.basicConfig(filename='/Users/admin/logs/data_analysis.log', level=logging.INFO)

try:
    df = pd.read_csv('/Users/admin/cleaned_data.csv')

    analysis_results = {
        'average_temperature': df['temperature'].mean(),
        'average_humidity': df['humidity'].mean(),
        'average_wind_speed': df['wind_speed'].mean(),
        'average_pressure': df['pressure'].mean(),
        'weather_distribution': df['weather'].value_counts().to_dict()
    }

    with open('/Users/admin/analysis_results.txt', 'w') as f:
        for key, value in analysis_results.items():
            f.write(f"{key}: {value}\n")

    logging.info("Data analysis completed successfully")
except Exception as e:
    logging.error(f"Error during data analysis: {e}")
    raise

