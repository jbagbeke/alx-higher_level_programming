#!/usr/bin/python3

""" Creates State and City from database """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, relationship
from relationship_city import City
from relationship_state import Base, State
import sys

if __name__ == '__main__':
    db_connect = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    session = Session(engine)

    new_city = City(name='San Francisco')
    new_state = State(name='California', cities=new_city)

    session.add(new_state)

    session.commit()
    session.close()
