-- lists all shows with or without genre
SELECT ts.title, tsg.genre_id FROM tv_shows ts left outer join tv_show_genres tsg On ts.id = tsg.show_id ORDER BY ts.title, tsg.genre_id ASC;
