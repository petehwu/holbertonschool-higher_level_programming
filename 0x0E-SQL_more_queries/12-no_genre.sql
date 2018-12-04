-- lists all shows without genre
SELECT ts.title, tsg.genre_id FROM tv_shows ts LEFT OUTER JOIN tv_show_genres tsg ON ts.id = tsg.show_id WHERE tsg.genre_id IS NULL ORDER BY ts.title, tsg.genre_id ASC;
