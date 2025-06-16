# 🚚 Delivery Time Prediction

This end-to-end machine learning project predicts **Estimated Time of Arrival (ETA)** for delivery orders based on factors like:

- Distance between pickup and drop-off locations
- Real-time traffic conditions
- Weather and temperature
- Order time and day of the week

---

## 🧩 Key Features

✅ Predict delivery time using **XGBoost Regression**  
✅ SQL for structured data storage and analysis  
✅ Power BI dashboards for **real-time delivery insights**  
✅ Optional **Dash web app** for interactive ETA prediction  
✅ Cleaned dataset and model pipeline ready to deploy

---

## 📁 Project Structure

```plaintext
delivery-time-prediction/
│
├── data/                      # Raw, processed, and export datasets
│   ├── raw/                   # Raw input (CSV)
│   ├── processed/             # Enriched + predictions
│   └── powerbi/               # Power BI CSV export
│
├── database/                 
│   ├── schema.sql             # SQL table definition
│   ├── insert_sample_data.sql
│   └── queries/               # SQL queries for Power BI insights
│
├── notebooks/                 # Jupyter notebooks: EDA, features, model
│
├── src/                       # Core ML & preprocessing scripts
│   ├── train_model.py
│   ├── predict_eta.py
│   └── enrich_with_*.py
│
├── scripts/                   # Helper scripts (e.g., export for BI)
├── dashboards/                # Power BI & Dash app
├── models/                    # Trained XGBoost model and scaler
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md

## 🧪 How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Load Sample Data

```bash
python scripts/export_to_sql.py
```
### 3. Train Model

```bash
python src/train_model.py
```
### 4. Predict on New Data
```bash
python src/predict_eta.py
```

## 📊 Power BI Dashboard

The .pbix file in dashboards/ shows:

- Delivery time averages by weather/traffic
- ETA prediction accuracy
- Daily delivery volume

## 🌐 Optional Dash Web App

To run the interactive ETA predictor:

```bash
python dashboards/dash_app.py
```
Then open your browser at: http://127.0.0.1:8050

## 📌 Sample Data Columns

| Column                  | Description                |
| ----------------------- | -------------------------- |
| `order_time`            | Timestamp of order         |
| `pickup_location`       | Pickup area (e.g. Toronto) |
| `drop_location`         | Destination                |
| `distance_km`           | Trip distance              |
| `traffic_level`         | Low / Medium / High        |
| `weather`               | Clear / Rain / Snow / Fog  |
| `temperature_c`         | Temperature in Celsius     |
| `delivery_time_minutes` | Actual delivery duration   |

## 📂 Model Output

After training, two files are saved:

- models/xgb_model.pkl — trained ML model
- models/scaler.pkl — fitted scaler for numeric features

## 🤝 Contributing

Feel free to fork this repo, add features, or submit issues.
You could integrate Google Maps API, OpenWeather API, or scale the app for real-time predictions.

