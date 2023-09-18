#!/usr/bin/python3
"""
Adds the State object “California” with the City “San Francisco”
to the database hbtn_0e_100_usa.
"""

if __name__ == "__main__":
    # Import necessary modules
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    # Create a database connection using user-provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create the necessary database tables based on defined models
    Base.metadata.create_all(engine)

    # Create a new session for database interaction
    session = Session(engine)

    # Create a new City object with the name "San Francisco"
    new_city = City(name='San Francisco')

    # Create a new State object with the name "California"
    new = State(name='California')

    # Establish a relationship between State and City objects
    new.cities.append(new_city)

    # Add both State and City objects to the session and commit changes
    session.add_all([new, new_city])
    session.commit()

    # Close the session
    session.close()
