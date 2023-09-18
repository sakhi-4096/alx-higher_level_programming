#!/usr/bin/python3
"""
List all cities of a given state from the "hbtn_0e_4_usa" database
using MySQLdb with protection against SQL injection.
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
    query = "SELECT cities.id, cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", [argv[4]]

    # Execute the query with state_name parameter
    cursor.execute(query)

    # Fetch all rows and display them
    cities = cursor.fetchall()
    j = []
    for city in cities:
        j.append(city[1])
    print(", ".join(j))

    # Close the cursor and connection
    cursor.close()
    connection.close()
