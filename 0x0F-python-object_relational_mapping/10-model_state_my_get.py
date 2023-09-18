#!/usr/bin/python3
"""
Print the State object with the name passed as an argument from the "hbtn_0e_6_usa"
database using SQLAlchemy and ensuring SQL injection safety
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state


def find_state_by_name(username, password, database_name, state_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query the database to find the State object with the provided state name
        state = session.query(State).filter(State.name == state_name).first()

        # Check if a State object was found
        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[
        1], sys.argv[2], sys.argv[3], sys.argv[4]
    find_state_by_name(username, password, database_name, state_name)
