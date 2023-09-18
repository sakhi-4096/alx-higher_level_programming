#!/usr/bin/python3
"""
Python script that takes four arguments and displays all values in
the "states" table of the "hbtn_0e_0_usa" database where the "name"
matches the provided argument while protecting against MySQL injections:
"""
import MySQLdb
from sys import argv


def search_states_safe(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            password=password,
            host='localhost',
            port=3306,
            database=database_name
        )

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Prepare the SQL query with the parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"

        # Execute the parameterized query with the user input
        cursor.execute(query, (state_name,))

        # Fetch all the rpws and display them
        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = argv[1], argv[2], argv[3], argv[4]
    search_states_safe(username, password, database_name, state_name)
