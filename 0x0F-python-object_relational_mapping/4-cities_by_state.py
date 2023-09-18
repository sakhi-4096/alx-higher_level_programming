#!/usr/bin/python3
"""
 List all cities from the "hbtn_0e_4_usa" database using MySQLdb
 with only one execute() statement.
"""
import MySQLdb
from sys import argv


def list_cities(username, password, database_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            password=password,
            host='locahost',
            port=3306,
            database=database_name
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the SQL query to retrieve all cities sorted by cities.id
        query = "SELECT * FROM cities ORDER BY cities.id"

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows and display them
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
    if len(argv) != 4:
        print("Usage: python 4-cities_by_state.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = argv[1], argv[2], argv[3]
    list_cities(username, password, database_name)
