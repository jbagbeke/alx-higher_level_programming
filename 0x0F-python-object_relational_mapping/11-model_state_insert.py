#!/usr/bin/python3

""" Adds the State object “Louisiana” to the database hbtn_0e_6_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == '__main__':
    db_connect = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    session1 = Session(engine)
    new_obj = State(name='Louisiana')

    session1.add(new_obj)
    session1.commit()

    result = session1.query(State).filter(State.name == 'Louisiana').all()

    for res in result:
        print(res.id)

    session1.close()
