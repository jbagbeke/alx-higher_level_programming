#!/usr/bin/python3

""" Prints the first State object from the database hbtn_0e_6_usa """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == '__main__':
    db_connect = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)
    sec_session = Session()

    if (sec_session.query(State).count() != 0):
        first = sec_session.query(State).first()
        print("{}: {}".format(first.id, first.name))
    esle:
        print('Nothing')

    sec_session.close()
