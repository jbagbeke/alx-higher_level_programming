#!/usr/bin/python3

""" Changes name of State object from the database hbtn_0e_6_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == '__main__':
    db_connect = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    session1 = Session(engine)

    result = session1.query(State).filter(State.id == 2).first()
    result.name = 'New Mexico'

    session1.commit()

    session1.close()
