#!/usr/bin/python3
"""
Define class 'City'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Define the City class similar to the State class, inheriting from Base and
    linking to the MySQL table "cities" with the specified attributes.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
