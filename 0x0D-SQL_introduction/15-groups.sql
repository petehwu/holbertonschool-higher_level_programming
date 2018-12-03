-- lists number of each score in table
SELECT score, sum(1) AS number FROM second_table GROUP BY score ORDER BY number DESC;
