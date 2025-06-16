import dash
from dash import dcc, html
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load model and scaler
model = joblib.load("models/xgb_model.pkl")
scaler = joblib.load("models/scaler.pkl")

app = dash.Dash(__name__)
app.title = "Delivery ETA Predictor"

traffic_options = ['Low', 'Medium', 'High']
weather_options = ['Clear', 'Rain', 'Snow', 'Fog']

app.layout = html.Div([
    html.H1("🚚 Delivery ETA Predictor", style={"textAlign": "center"}),
    
    html.Div([
        html.Label("Distance (km):"),
        dcc.Input(id="distance", type="number", value=10, step=0.1)
    ]),

    html.Div([
        html.Label("Traffic Level:"),
        dcc.Dropdown(id="traffic", options=[{"label": i, "value": i} for i in traffic_options], value="Medium")
    ]),

    html.Div([
        html.Label("Weather Condition:"),
        dcc.Dropdown(id="weather", options=[{"label": i, "value": i} for i in weather_options], value="Clear")
    ]),

    html.Div([
        html.Label("Temperature (°C):"),
        dcc.Input(id="temperature", type="number", value=20, step=0.5)
    ]),

    html.Br(),
    html.Button("Predict ETA", id="predict-button", n_clicks=0),
    html.Div(id="output", style={"marginTop": "20px", "fontSize": "20px", "fontWeight": "bold"})
])

@app.callback(
    dash.dependencies.Output("output", "children"),
    [dash.dependencies.Input("predict-button", "n_clicks")],
    [dash.dependencies.State("distance", "value"),
     dash.dependencies.State("traffic", "value"),
     dash.dependencies.State("weather", "value"),
     dash.dependencies.State("temperature", "value")]
)
def predict_eta(n_clicks, distance, traffic, weather, temperature):
    if n_clicks == 0:
        return ""
    
    input_dict = {
        "distance_km": distance,
        "temperature_c": temperature,
        "hour": 14,  # default/static
        "day_of_week": 2,  # default/static
        "traffic_level_Medium": 1 if traffic == "Medium" else 0,
        "traffic_level_High": 1 if traffic == "High" else 0,
        "weather_Fog": 1 if weather == "Fog" else 0,
        "weather_Rain": 1 if weather == "Rain" else 0,
        "weather_Snow": 1 if weather == "Snow" else 0,
    }

    # Ensure all columns match training
    feature_vector = pd.DataFrame([input_dict])
    feature_vector_scaled = scaler.transform(feature_vector)

    prediction = model.predict(feature_vector_scaled)[0]
    return f"Estimated Delivery Time: {round(prediction, 2)} minutes"

if __name__ == "__main__":
    app.run_server(debug=True)
