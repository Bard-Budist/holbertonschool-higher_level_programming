-- Cites of california
SELECT cities.id, cities.name FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';
