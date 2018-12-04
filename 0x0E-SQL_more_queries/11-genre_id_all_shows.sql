-- lists all shows with or without genre
SELECT ts.title, tsg.genre_id FROM tv_shows ts LEFT OUTER JOIN tv_show_genres tsg ON ts.id = tsg.show_id ORDER BY ts.title, tsg.genre_id ASC;
