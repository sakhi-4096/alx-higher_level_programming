-- create the database hbtn_0d_usa and the table cities
-- description of table data:
--      id INT unique, auto generated, cannot be null and primary key
--      state_id INT, cannot be null and FOREIGN KEY references to id of the states
--      name VARCHAR(256), can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
