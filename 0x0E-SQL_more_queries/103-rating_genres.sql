-- Show rates by Genres
SELECT tv_genres.name AS name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres, tv_show_genres, tv_show_ratings WHERE tv_show_ratings.show_id = tv_show_genres.show_id and tv_show_genres.genre_id=tv_genres.id GROUP BY name ORDER BY rating DESC;
