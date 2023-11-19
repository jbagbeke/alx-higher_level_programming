#!/usr/bin/python3

""" Deletes all State objects with name containing letter a from database  """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == '__main__':
    db_connect = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)

    Session = sessionmaker(bind=engine)
    session1 = Session()

    cmd = State.name.like('%a%')
    result = session1.query(State).filter(cmd).all()

    for res in result:
        session1.delete(res)

    session1.commit()
    session1.close()
