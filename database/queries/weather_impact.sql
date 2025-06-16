-- Delivery time averages by weather condition
SELECT 
    weather,
    COUNT(*) AS total_deliveries,
    AVG(delivery_time_minutes) AS avg_time
FROM deliveries
GROUP BY weather;
