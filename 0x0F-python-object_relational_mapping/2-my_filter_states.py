#!/usr/bin/python3
"""
A script that takes an argument and displays all values in the
"states" table of the "hbtn_0e_0_usa" database where the "name"
matches the provided argument.
"""
import MySQLdb
import sys


def search_states(username, password, database_name, state_name):
    # Connect to the MySQL server
    connection = MySQLdb.connect(
        user=username,
        passwd=password,
        host='localhost',
        port=3306,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Prepare the SQL query with the user input and execute it
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch all the rows and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    username, password, database_name, state_name = sys.argv[
        1], sys.argv[2], sys.argv[3], sys.argv[4]
    search_states(username, password, database_name, state_name)
