-- lists all genre not linked to Dexter
SELECT 	DISTINCT(tv_genres.name) FROM tv_genres, tv_show_genres WHERE
tv_genres.id = tv_show_genres.genre_id AND
tv_show_genres.genre_id NOT IN 
(SELECT DISTINCT(tv_show_genres.genre_id) FROM tv_show_genres, tv_shows WHERE
tv_shows.id = tv_show_genres.show_id AND
tv_shows.title = 'Dexter')
ORDER BY 1 ASC;
