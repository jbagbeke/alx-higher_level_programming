#!/usr/bin/python3

""" Prints all City objects from the database hbtn_0e_14_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
import sys


if __name__ == '__main__':
    db_connect = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    session1 = Session(engine)

    cities = session1.query(City).order_by(City.id).all()

    for city in cities:
        state = city.state
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session1.close()
