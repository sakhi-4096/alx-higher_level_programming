#!/usr/bin/python3
"""
A script that lists all State objects from the "hbtn_0e_6_usa"
database using SQLAlchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state


def list_states(username, password, database_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query the database to retrieve all State objects and order them by states.id
        states = session.query(State).order_by(State.id).all()

        # Print the State objects
        for state in states:
            print(f"{state.id}: {state.name}")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
