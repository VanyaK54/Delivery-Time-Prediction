INSERT INTO deliveries (
    order_id, order_time, pickup_location, drop_location,
    distance_km, traffic_level, weather, temperature_c, delivery_time_minutes
)
VALUES
(1, '2024-07-02 14:24:00', 'Toronto', 'Brampton', 16.02, 'Low', 'Clear', 19.97, 28.69),
(2, '2024-07-07 12:55:00', 'Toronto', 'North York', 6.43, 'Low', 'Rain', 13.62, 12.13),
(3, '2024-07-08 04:23:00', 'Toronto', 'Scarborough', 37.22, 'High', 'Fog', 21.48, 121.48),
(4, '2024-07-08 00:54:00', 'Scarborough', 'Toronto', 39.15, 'Low', 'Fog', 30.23, 82.83),
(5, '2024-07-03 02:27:00', 'Mississauga', 'Brampton', 9.60, 'Medium', 'Clear', 12.66, 19.52);
