#!/usr/bin/python3
"""
List all states from the "hbtn_0e_0_usa" database using the MySQLdb module.
"""
import MySQLdb
from sys import argv


def list_states(username, password, database_name):
    # Connect to the MySQL server
    connection = MySQLdb.connect(
        user=username,
        password=password,
        host='localhost',
        port=3306,
        database=database_name
    )
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to retreive states sorted by states.id
    cursor.execute("SELCT * FROM states ORDER BY states.id")

    # Fetch all the rows and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    list_states(username, password, database_name)
