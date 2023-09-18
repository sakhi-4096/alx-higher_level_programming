#!/usr/bin/python3
"""
Python script that takes four arguments and displays all values in
the "states" table of the "hbtn_0e_0_usa" database where the "name"
matches the provided argument while protecting against MySQL injections:
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the MySQL server
    connection = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        host='localhost',
        port=3306,
        db=argv[3]
    )

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Prepare the SQL query with the parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"

    # Execute the parameterized query with the user input
    cursor.execute(query, (argv[4],))

    # Fetch all the rpws and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()
