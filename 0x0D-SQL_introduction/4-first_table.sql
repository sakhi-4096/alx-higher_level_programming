-- create table; should not fail if exists
-- cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
