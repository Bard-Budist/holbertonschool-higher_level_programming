-- Temperatures
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE temperatures.month BETWEEN 7 and 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3
