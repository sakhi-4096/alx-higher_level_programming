#!/usr/bin/python3
"""
List all states from the "hbtn_0e_0_usa" database using the MySQLdb module.
"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            password=password,
            host='localhost',
            port=3306
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

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
