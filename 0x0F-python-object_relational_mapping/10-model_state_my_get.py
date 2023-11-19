#!/usr/bin/python3

""" Prints State object with name passed as arg from db hbtn_0e_6_usa """
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

    session1 = Session()

    results = session1.query(State).filter(State.name == sys.argv[4]).all()

    if (results):
        for result in results:
            print(result.id)
    else:
        print('Not found')

    session1.close()
