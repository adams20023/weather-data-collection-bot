import pandas as pd
import logging

logging.basicConfig(filename='/Users/admin/logs/data_cleaning.log', level=logging.INFO)

try:
    df = pd.read_csv('/Users/admin/output_data.csv')

    if {'temperature', 'weather', 'humidity', 'wind_speed', 'pressure'}.issubset(df.columns):
        df['temperature'] = df['temperature'] - 273.15  # Convert from Kelvin to Celsius
        df.to_csv('/Users/admin/cleaned_data.csv', index=False)
        logging.info("Data cleaning completed successfully")
    else:
        logging.error("Missing one or more required columns in the data.")
        raise ValueError("Missing one or more required columns in the data.")
except Exception as e:
    logging.error(f"Error during data cleaning: {e}")
    raise

