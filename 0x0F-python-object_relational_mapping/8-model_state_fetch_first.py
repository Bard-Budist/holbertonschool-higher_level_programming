#!/usr/bin/python3
"""Task 08"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).first()
    if (first is not None):
        print("{:d}: {}".format(first.id, first.name))
    else:
        print("Nothing")
