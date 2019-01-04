#!/usr/bin/python3
"""python script to list all state objects
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], 
                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.bind=engine

    DBSession=sessionmaker(bind=engine)
    session=DBSession()
    first=session.query(State).first()
    if (first is None):
        print("Nothing")
    else:
        print("{:d}: {:s}".format(first.id, first.name))
