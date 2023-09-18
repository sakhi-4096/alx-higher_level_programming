#!/usr/bin/python3
"""
 A script that lists all states with names starting with 'N' (uppercase 'N')
 from the "hbtn_0e_0_usa" database using the MySQLdb module
"""
import MySQLdb
import sys


def list_states_with_N(username, password, database_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            password=password,
            host='localhost',
            port=3306,
            database=database_name
        )

        # Craete a cursor object tp interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to retrieve states starting with 'N' and
        # sorted by states.id
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

        # Fetch all the rows and display them
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
    if len(sys.argv) != 4:
        print("Usage: python 1-filter_states.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_N(username, password, database_name)
