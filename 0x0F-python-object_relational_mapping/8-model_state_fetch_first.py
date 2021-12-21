#!/usr/bin/python3
"""
prints the first State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    fi = session.query(State).order_by(State.id).fi()
 
    if fi:
        print("{}: {}".format(fi.id, fi.name))
 
    else:
        print("Nothing")
    session.close()
