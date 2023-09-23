#!/usr/bin/python3
"""
List all states from the "hbtn_0e_0_usa" database using the MySQLdb module.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # connect to the MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # create a cursor object to interact with the database
    cursor = connection.cursor()
    # execute the SQL query to retreive states sorted by states.id
    cursor.execute("SELCT * FROM states ORDER BY states.id ASC")

    # fetch all the rows and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    connection.close()
