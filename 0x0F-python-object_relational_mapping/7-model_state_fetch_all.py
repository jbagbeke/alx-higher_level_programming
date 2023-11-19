#!/usr/bin/python3

""" Lists all State objects from the database hbtn_0e_6_usa """
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    connect = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                       sys.argv[2],
                                                       sys.argv[3])
    engine = create_engine(connect)
    Session = sessionmaker(bind=engine)

    sec_session = Session()

    results = sec_session.query(State).order_by(State.id).all()

    for result in results:
        print("{}: {}".format(result.id, result.name))

    sec_session.close()
