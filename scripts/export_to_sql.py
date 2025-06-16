import pandas as pd 
from sqlalchemy import create_engine
import Pylance

def export_csv_to_sql(csv_path, db_path="sqlite:///deliveries.db"):
    df = pd.read_csv(csv_path)
    engine = create_engine(db_path)
    df.to_sql("deliveries", con=engine, if_exists="replace", index=False)
    print("✅ Data successfully exported to SQL.")

if __name__ == "__main__":
    export_csv_to_sql("data/raw/delivery_records.csv")
