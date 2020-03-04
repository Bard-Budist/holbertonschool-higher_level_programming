-- SHow more
SELECT tv_show.title, tv_show_genres.genre_id FROM tv_show
INNER JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_show.title ASC
