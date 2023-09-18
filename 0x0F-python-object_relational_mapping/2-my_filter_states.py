#!/usr/bin/python3
"""
A script that takes an argument and displays all values in the
"states" table of the "hbtn_0e_0_usa" database where the "name"
matches the provided argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the database
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor to execute queries using SQL; match argument given
    db_cursor = db_connection.cursor()

    # Prepare the SQL query with the user input and execute it
    query = """SELECT * FROM states
                WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    db_cursor.execute(query)

    # Fetch and print matching rows
    for row in db_cursor.fetchall():
        if row[1] == state_name:
            print(row)

    # Close the cursor and database connection
    db_cursor.close()
    db_connection.close()
