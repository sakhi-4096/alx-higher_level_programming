#!/usr/bin/python3
"""
 List all cities from the "hbtn_0e_4_usa" database using MySQLdb
 with only one execute() statement.
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

    #  Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Define SQL query with a parameterized query to retriev cities by state
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON cities.states_id = states.id \
            ORDER BY cities.id ASC"

    # Execute the query with state_name parameter
    cursor.execute(query)

    # Fetch all rows and display them
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and connection
    cursor.close()
    connection.close()
