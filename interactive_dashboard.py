import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import logging

logging.basicConfig(filename='/Users/admin/logs/interactive_dashboard.log', level=logging.INFO)

try:
    df = pd.read_csv('/Users/admin/cleaned_data.csv')

    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1("Weather Data Dashboard"),
        dcc.Graph(id='temperature-histogram'),
        dcc.Graph(id='humidity-histogram'),
        dcc.Graph(id='weather-pie-chart'),
    ])

    @app.callback(
        dash.dependencies.Output('temperature-histogram', 'figure'),
        dash.dependencies.Output('humidity-histogram', 'figure'),
        dash.dependencies.Output('weather-pie-chart', 'figure'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
    def update_graphs(n):
        fig1 = px.histogram(df, x='temperature', title='Temperature Distribution')
        fig2 = px.histogram(df, x='humidity', title='Humidity Distribution')
        fig3 = px.pie(df, names='weather', title='Weather Distribution')

        return fig1, fig2, fig3

    app.run_server(debug=True)

    logging.info("Interactive dashboard started successfully")
except Exception as e:
    logging.error(f"Error during interactive dashboard setup: {e}")
    raise

