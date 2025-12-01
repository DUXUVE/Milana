SELECT * FROM netflix_shows;

SELECT title, release_year FROM netflix_shows WHERE type = 'Movie';

SELECT title, director FROM netflix_shows WHERE type = 'Show' AND rating > 8.0;

SELECT id, type, description FROM netflix_shows WHERE description ILIKE '%love%';

SELECT * FROM netflix_shows ORDER BY release_year DESC LIMIT 10;