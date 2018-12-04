-- list all shows by genre
SELECT tv_shows.title, tv_genres.name FROM tv_shows left outer join tv_show_genres
ON tv_shows.id = tv_show_genres.show_id left outer join tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 1, 2 ASC;
