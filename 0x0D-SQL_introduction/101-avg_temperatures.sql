-- Displays the average temperature (fahr) by city ordered by temperature (desc)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
