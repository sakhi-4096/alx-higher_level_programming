-- import a SQL dump
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- does not have a genre, display NULL in genre column
-- display: tv_shows.title - tv_genres.name
-- sort in ascending order by the show title and genre name

    SELECT tv_shows.title, tv_genres.name
      FROM tv_shows
 LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
 LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
  ORDER BY tv_shows.title, tv_genres.name ASC;
