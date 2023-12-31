#!/usr/bin/python3

""" Lists all State objects, and corresponding City objects """
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
import sys

if __name__ == '__main__':
    db_connect = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    
    for result in session.query(State).order_by(State.id).all():
        print("{}: {}".format(result.id, result.name))
        
        for city in result.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
