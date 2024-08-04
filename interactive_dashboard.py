import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import logging

# Configure logging
logging.basicConfig(filename='/Users/admin/logs/interactive_dashboard.log', level=logging.DEBUG)

# Initialize Dash app
app = dash.Dash(__name__)

# Load the data
def load_data():
    try:
        data = pd.read_csv('/Users/admin/output_data.csv')
        logging.info("Data loaded successfully")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Weather Data Dashboard"),
    
    dcc.Graph(id='temperature-histogram'),
    dcc.Graph(id='humidity-histogram'),
    dcc.Graph(id='weather-pie-chart'),
    
    dcc.Interval(
        id='interval-component',
        interval=60*60*1000,  # Update every hour
        n_intervals=0
    )
])

# Define callback to update graphs
@app.callback(
    [Output('temperature-histogram', 'figure'),
     Output('humidity-histogram', 'figure'),
     Output('weather-pie-chart', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n_intervals):
    data = load_data()
    if data.empty:
        logging.warning("No data available for plotting")
        return {}, {}, {}

    # Temperature Histogram
    temp_fig = px.histogram(data, x='temp', title='Temperature Distribution')

    # Humidity Histogram
    humidity_fig = px.histogram(data, x='humidity', title='Humidity Distribution')

    # Weather Pie Chart
    weather_counts = data['weather_description'].value_counts()
    pie_fig = px.pie(values=weather_counts.values, names=weather_counts.index, title='Weather Conditions Distribution')

    return temp_fig, humidity_fig, pie_fig

# Run the app
def start_dashboard():
    logging.info("Starting interactive dashboard")
    app.run_server(debug=True)

if __name__ == "__main__":
    start_dashboard()
