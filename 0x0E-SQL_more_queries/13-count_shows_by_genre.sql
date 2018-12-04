-- list all genre and list number of shows
SELECT a.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres a, tv_show_genres b WHERE a.id = b.genre_id GROUP BY a.name ORDER BY number_of_shows DESC;
