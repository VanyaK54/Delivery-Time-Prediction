import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import os

from src.data_prep import load_data, preprocess

# === CONFIG ===
DATA_PATH = "data/raw/delivery_records.csv"
MODEL_PATH = "models/xgb_model.pkl"
SCALER_PATH = "models/scaler.pkl"

def train():
    print("🔹 Loading data...")
    df = load_data(DATA_PATH)
    df = preprocess(df)

    X = df.drop(columns=["order_id", "order_time", "delivery_time_minutes"])
    y = df["delivery_time_minutes"]

    print("🔹 Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("🔹 Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("🔹 Training XGBoost model...")
    model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    model.fit(X_train_scaled, y_train)

    print("🔹 Evaluating model...")
    preds = model.predict(X_test_scaled)
    rmse = mean_squared_error(y_test, preds, squared=False)
    print(f"✅ RMSE on test set: {rmse:.2f} minutes")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print(f"✅ Model saved to {MODEL_PATH}")
    print(f"✅ Scaler saved to {SCALER_PATH}")

if __name__ == "__main__":
    train()
