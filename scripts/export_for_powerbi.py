import pandas as pd

def export_selected_columns(input_path, output_path):
    df = pd.read_csv(input_path)
    columns_to_export = [
        "order_id", "order_time", "pickup_location", "drop_location",
        "distance_km", "traffic_level", "weather", "temperature_c", "delivery_time_minutes"
    ]
    df[columns_to_export].to_csv(output_path, index=False)
    print(f"✅ Exported clean file for Power BI: {output_path}")

if __name__ == "__main__":
    export_selected_columns("data/raw/delivery_records.csv", "data/powerbi/delivery_clean.csv")
