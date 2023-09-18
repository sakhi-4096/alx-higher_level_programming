#!/usr/bin/python3
"""
Print the first State object from the "hbtn_0e_6_usa" database using
SQLAlchemy and without fetching all states
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state


def print_first_state(username, password, database_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query the database to retrieve the first State object by ordering by states.id
        first_state = session.query(State).order_by(State.id).first()

        # Check if a State object was found
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    print_first_state(username, password, database_name)
