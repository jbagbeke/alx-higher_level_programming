-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tv_genres.name AS name
	FROM tv_show_genres
	JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	AND tv_shows.title = 'Dexter'
	JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id;
