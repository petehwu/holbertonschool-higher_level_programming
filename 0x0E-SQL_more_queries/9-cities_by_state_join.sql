-- lists all cities and state using join
SELECT c.id, c.name, s.name FROM cities c, states s WHERE c.state_id = s.id ORDER BY c.id ASC;
