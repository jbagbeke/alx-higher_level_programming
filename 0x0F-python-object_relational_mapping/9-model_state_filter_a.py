#!/usr/bin/python3

""" Lists State objects containing the letter a from database hbtn_0e_6_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base

if __name__ == '__main__':
    db_connect = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)

    session_one = Session()

    results = session_one.query(State).filter(State.name.like('%a%'))

    for result in results:
        print("{}: {}".format(result.id, result.name))

    session_one.close()
