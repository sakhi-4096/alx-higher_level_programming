#!/usr/bin/python3
"""
Define class 'State'
"""

# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance for defineing classes
Base = declarative_base()


class State(Base):
    # Set the table name in the database
    __tablename__ = 'states'

    # Define the 'id' column, which is an auto-generated unique integer, primary key and can't be null
    id = Column(Integer, primary_key=True, nullable=False)

    # Define the 'name' column, which is a string with a maximum of 128 characters and can't be null
    name = Column(String(128), nullable=False)
