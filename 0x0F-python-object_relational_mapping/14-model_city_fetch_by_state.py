#!/usr/bin/python3
"""python script to list all state objects
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cities = session.query(City).all()
    for c in cities:
        state = session.query(State).filter(State.id == c.state_id).first()
        print("{:s}: ({:d}) {:s}".format(state.name, c.id, c.name))
