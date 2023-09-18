#!/usr/bin/python3
"""
Change the name of a State object in the "hbtn_0e_6_usa" database using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state


def change_state_name(username, password, database_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Find the State object with id = 2
        state_to_change = session.query(State).filter_by(id=2).first()

        # Check if a State object with id = 2 exists
        if state_to_change:
            # Change the name of the State object to "New Mexico"
            state_to_change.name = "New Mexico"

            # Commit the change to the database
            session.commit()
        else:
            print("State with id=2 not found")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    change_state_name(username, password, database_name)
