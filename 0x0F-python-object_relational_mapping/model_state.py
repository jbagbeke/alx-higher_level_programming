#!/usr/bin/python3

""" Class definition of a State using SQLAlchemy """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sys

Base = declarative_base()


class State(Base):
    """ Inherits from Base """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)


connect = 'mysql://' + sys.argv[1] + ':' + sys.argv[2] + '@' + 'localhost'
engine = create_engine(connect + ':' + '3306' + '/' + sys.argv[3])
Base.metadata.create_all(engine)
