-- Lists all records of the table second_table of the database hbtn_0c_0
-- Do not list rows without a name value
-- Display the score and the name (in this order)
-- In descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
