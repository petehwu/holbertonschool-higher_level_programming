-- lists shows by rating
SELECT a.title, SUM(b.rate) AS rating FROM tv_shows a, tv_show_ratings b
WHERE a.id = b.show_id 
GROUP BY b.show_id
ORDER BY 2 DESC;
