#!/bin/bash

# Activate the virtual environment
source /Users/admin/myenv/bin/activate

# Run the Python scripts
echo "Starting data collection..."
python /Users/admin/data_collection.py >> /Users/admin/logs/data_collection.log 2>&1

echo "Starting data cleaning..."
python /Users/admin/data_cleaning.py >> /Users/admin/logs/data_cleaning.log 2>&1

echo "Starting data analysis..."
python /Users/admin/data_analysis.py >> /Users/admin/logs/data_analysis.log 2>&1

echo "Starting interactive dashboard..."
python /Users/admin/interactive_dashboard.py >> /Users/admin/logs/interactive_dashboard.log 2>&1

echo "All tasks completed."

