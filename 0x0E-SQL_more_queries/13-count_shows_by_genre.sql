-- import a SQL dum
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- list genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- display: tv_genres.name - number_shows
-- don’t display genre that doesn’t have any shows linked
-- sort in descending order by the number of shows linked

    SELECT tv_genres.name AS genre, COUNT(*) AS 'number_shows'
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY genre
  ORDER BY number_shows DESC;
