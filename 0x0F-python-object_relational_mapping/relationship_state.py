#!/usr/bin/python3

""" Class definition of a State using SQLAlchemy """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Inherits from Base """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cscd = 'all, delete-orphan'
    cities = relationship('City', back_populates='state', cascade=cscd)
