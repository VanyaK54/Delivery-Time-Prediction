CREATE TABLE deliveries (
    order_id INTEGER PRIMARY KEY,
    order_time TIMESTAMP,
    pickup_location TEXT,
    drop_location TEXT,
    distance_km REAL,
    traffic_level TEXT,
    weather TEXT,
    temperature_c REAL,
    delivery_time_minutes REAL
);
