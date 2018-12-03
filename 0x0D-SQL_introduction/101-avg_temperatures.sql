-- display average temp by city order by temp desc
SELECT city, SUM(value)/COUNT(*) AS avg_temp FROM temperatures GROUP BY city, state ORDER BY avg_temp DESC;
