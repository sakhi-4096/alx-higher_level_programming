#!/usr/bin/python3
"""
This module defines the State class, representing the states table
in the database.
"""

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The primary key for the state.
        name (str): The name of the state.
        cities (relationship): A relationship to City objects associated with
        this state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
