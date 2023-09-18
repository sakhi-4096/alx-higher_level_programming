#!/usr/bin/python3
"""
Add the State object "Louisiana" to the "hbtn_0e_6_usa" database using SQLAlchemy
and print the new states.id after creation
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state


def add_louisiana(username, password, database_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Create a new State object for Louisiana
        louisiana_state = State(name="Louisiana")

        # Add the new State object to the session and commit it to the database
        session.add(louisiana_state)
        session.commit()

        # Print the new states.id after creation
        print(louisiana_state.id)

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    add_louisiana(username, password, database_name)
