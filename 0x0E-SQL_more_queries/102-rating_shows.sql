-- SUM of ratings by show
SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows, tv_show_ratings WHERE tv_show_ratings.show_id = tv_shows.id GROUP BY title ORDER BY rating DESC;
