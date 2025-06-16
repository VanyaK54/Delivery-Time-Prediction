import pandas as pd
import joblib
from src.data_prep import preprocess

MODEL_PATH = "models/xgb_model.pkl"
SCALER_PATH = "models/scaler.pkl"
DATA_PATH = "data/raw/delivery_records.csv"

def predict():
    df = pd.read_csv(DATA_PATH)
    df = preprocess(df)

    X = df.drop(columns=["order_id", "order_time", "delivery_time_minutes"])

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    X_scaled = scaler.transform(X)
    predictions = model.predict(X_scaled)
    df["predicted_eta"] = predictions

    df[["order_id", "delivery_time_minutes", "predicted_eta"]].to_csv("data/processed/predictions.csv", index=False)
    print("✅ Predictions saved to data/processed/predictions.csv")

if __name__ == "__main__":
    predict()
