import pandas as pd

def load_data(path):
    """
    Load delivery records from CSV.
    """
    df = pd.read_csv(path)
    df['order_time'] = pd.to_datetime(df['order_time'])
    return df

def preprocess(df):
    """
    Add time features and encode categorical variables.
    """
    df['hour'] = df['order_time'].dt.hour
    df['day_of_week'] = df['order_time'].dt.dayofweek

    df = pd.get_dummies(df, columns=['traffic_level', 'weather'], drop_first=True)
    return df
