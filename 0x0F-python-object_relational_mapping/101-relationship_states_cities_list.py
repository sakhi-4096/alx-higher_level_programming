#!/usr/bin/python3
"""
Script to retrieve and display states and their associated cities using
SQLAlchemy.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # check for the correct number of command-line arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # create a database engine and establish a connection
    db_connection_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_connection_url, pool_pre_ping=True)

    # create the tables if they do not exist
    Base.metadata.create_all(engine)

    # create a session to interact with the database
    session = Session(engine)

    # cquery and display all states and their associated cities
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("State ID: {} - Name: {}".format(state.id, state.name))
        for city in state.cities:
            print("    City ID: {} - Name: {}".format(city.id, city.name))

    # commit the changes to the database and close the session
    session.commit()
    session.close()
