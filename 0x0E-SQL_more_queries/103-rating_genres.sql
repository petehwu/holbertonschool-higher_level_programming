-- shows ratings by genre
SELECT a.name, SUM(c.rate) AS rating FROM tv_genres a, tv_show_genres b, tv_show_ratings c
WHERE a.id = b.genre_id AND 
b.show_id = c.show_id 
GROUP BY b.genre_id ORDER BY 2 desc;
