#!/usr/bin/python3
"""
Define class 'City'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class that inherits from Base

    Attributes:
        id: Id city
        name: Name of the city
        state_id: State id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
