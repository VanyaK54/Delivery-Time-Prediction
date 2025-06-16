# Simulated example of how to enrich dataset with weather
# In production, you would use OpenWeatherMap or similar APIs

import pandas as pd

def simulate_weather_enrichment(input_path, output_path):
    df = pd.read_csv(input_path)
    df['weather'] = "Clear"  # Static value for simulation
    df.to_csv(output_path, index=False)
    print(f"✅ Weather enriched data saved to {output_path}")

if __name__ == "__main__":
    simulate_weather_enrichment("data/raw/delivery_records.csv", "data/processed/weather_enriched.csv")
