#!/bin/bash

# Create logs directory if it does not exist
mkdir -p /Users/admin/logs

# Run data collection
echo "Starting data collection..."
python /Users/admin/weather_data_collection/data_collection.py

# Run data cleaning
echo "Starting data cleaning..."
python /Users/admin/weather_data_collection/data_cleaning.py

# Run data analysis
echo "Starting data analysis..."
python /Users/admin/weather_data_collection/data_analysis.py

# Run interactive dashboard
echo "Starting interactive dashboard..."
python /Users/admin/weather_data_collection/interactive_dashboard.py

echo "All tasks completed."

