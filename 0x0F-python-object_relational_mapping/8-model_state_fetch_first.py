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

    first_one = sec_session.query(State).first()

    if (not first_one):
        print ('')
    else:
        print("{}: {}".format(first_one.id, first_one.name))

    sec_session.close()
