-- Delivery time averages by traffic level
SELECT 
    traffic_level,
    COUNT(*) AS total_deliveries,
    AVG(delivery_time_minutes) AS avg_time
FROM deliveries
GROUP BY traffic_level;
