-- lists everything except comedy
SELECT a.title FROM tv_shows a WHERE 
a.id NOT IN (
SELECT a.show_id FROM tv_show_genres a, tv_genres b WHERE
a.genre_id = b.id AND
b.name = 'Comedy')
 ORDER BY 1 ASC;
