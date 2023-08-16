-- import a SQL dump
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- list all Comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy
-- display: tv_shows.title
-- sorte in ascending order by the show title

    SELECT tv_shows.title
      FROM tv_shows
INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
     WHERE tv_genres.name = "Comedy"
  ORDER BY tv_shows.title ASC;
