-- lists all comedy shows only
SELECT tv_shows.title FROM tv_shows, tv_show_genres, tv_genres WHERE tv_genres.name = 'Comedy' AND tv_genres.id = tv_show_genres.genre_id AND tv_show_genres.show_id = tv_shows.id ORDER BY 1 ASC;
