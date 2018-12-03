-- displays top 3 city temps for July and August
SELECT city, SUM(value)/COUNT(*) AS avg_temp FROM temperatures WHERE month IN (7,8) GROUP BY city, state ORDER BY avg_temp DESC LIMIT 3;;
