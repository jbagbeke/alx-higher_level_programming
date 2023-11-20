#!/usr/bin/python3

""" Contains the class definition of a City """
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base
from sqlalchemy import create_engine
import sys


class City(Base):
    """ Links to the MySQL table cities """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
