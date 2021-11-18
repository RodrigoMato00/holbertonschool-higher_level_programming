-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT title, SUM(tv_show_ratings.rate) as rating
FROM tv_shows
INNER JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show.id
GROUP BY tv_shows.id
ORDER BY rating DESC;
