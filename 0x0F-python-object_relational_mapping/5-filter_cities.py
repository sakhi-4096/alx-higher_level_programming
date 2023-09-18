#!/usr/bin/python3
"""
List all cities of a given state from the "hbtn_0e_4_usa" database
using MySQLdb with protection against SQL injection.
"""
import MySQLdb
from sys import argv


def list_cities_by_state(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            password=password,
            host='localhost',
            port=3306,
            database=database_name
        )

        #  Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define SQL query with a parameterized query to retriev cities by state
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.states_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id"

        # Execute the query with state_name parameter
        cursor.execute(query, (state_name,))

        # Fetch all rows and display them
        cities = cursor.fetchall()
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: python 5-filter_cities.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = argv[1], argv[2], argv[3], argv[4]
    list_cities_by_state(username, password, database_name, state_name)
