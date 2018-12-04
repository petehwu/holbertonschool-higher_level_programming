-- selects cities within california without using join
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE UPPER(name) = 'CALIFORNIA') ORDER BY cities.id ASC;
