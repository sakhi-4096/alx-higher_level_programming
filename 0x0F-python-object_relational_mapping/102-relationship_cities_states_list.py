#!/usr/bin/python3
"""
Script to list all City objects from the database hbtn_0e_101_usa.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    # check for the correct number of command-line arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # create a database engine and establish a connection
    db_connection_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_connection_url)

    # create the tables if they do not exist
    Base.metadata.create_all(engine)

    # create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # query and display all City objects and their associated State
    cities = session.query(City).all()

    for city in cities:
        print("City ID: {} - Name: {} -> State: {}".format(city.id,
              city.name, city.state.name))

    # close the session
    session.close()
