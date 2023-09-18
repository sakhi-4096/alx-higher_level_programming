#!/usr/bin/python3
"""
Print all City objects from the "hbtn_0e_14_usa" database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City  # Import City class from model_city


def fetch_cities_by_state(username, password, database_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query the database to retrieve City objects sorted by cities.id
        cities = session.query(City).order_by(City.id).all()

        # Print the City objects in the specified format
        for city in cities:
            state_name = session.query(State.name).filter(
                State.id == city.state_id).first()[0]
            print(f"{state_name}: ({city.id}) {city.name}")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, database_name)
