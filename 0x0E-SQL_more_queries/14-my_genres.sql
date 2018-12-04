-- lists all genres of Dexter show
SELECT DISTINCT(tv_genres.name) FROM tv_shows, tv_show_genres, tv_genres WHERE tv_shows.title = 'Dexter' AND tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id ORDER by tv_genres.name ASC;
