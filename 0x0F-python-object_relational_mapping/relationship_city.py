#!/usr/bin/python3
"""
This module defines the City class, representing the cities table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Represents a city in the database.

    Attributes:
        id (int): The primary key for the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the associated state's
        primary key.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
