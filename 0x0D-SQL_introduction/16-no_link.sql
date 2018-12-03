-- lists all rows where name has value
SELECT score, name FROM second_table WHERE name IS NOT NULL and name != "" ORDER BY score DESC;
