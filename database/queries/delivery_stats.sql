-- Average delivery time by day
SELECT 
    strftime('%Y-%m-%d', order_time) AS delivery_day,
    COUNT(*) AS total_deliveries,
    AVG(delivery_time_minutes) AS avg_delivery_time
FROM deliveries
GROUP BY delivery_day;
