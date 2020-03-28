#!/usr/bin/python3
"""Task 14"""
import sys
from model_state import State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    State.cities = relationship("City", back_populates="state_rel")

    for s, c in session.query(State, City).\
        filter(State.id == City.state_id).\
            order_by(City.id):
        print("{}: ({:d}) {}".format(s.name, c.id, c.name))
