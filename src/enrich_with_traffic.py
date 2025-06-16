# Simulated example of how to enrich dataset with traffic levels
# In production, you would use Google Maps API or similar

import pandas as pd

def simulate_traffic_enrichment(input_path, output_path):
    df = pd.read_csv(input_path)
    df['traffic_level'] = "Medium"  # Static value for simulation
    df.to_csv(output_path, index=False)
    print(f"✅ Traffic enriched data saved to {output_path}")

if __name__ == "__main__":
    simulate_traffic_enrichment("data/raw/delivery_records.csv", "data/processed/traffic_enriched.csv")
