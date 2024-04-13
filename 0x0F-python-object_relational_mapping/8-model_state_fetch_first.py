#!/usr/bin/python3
""" Script that prints the first State object from
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import select, create_engine
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    with engine.connect() as con:
        s = select(State).order_by(State.id)
        result = con.execute(s)
        first_state = result.first()
        if first_state is None:
            print("Nothing")
        else:
            print('{}: {}'.format(first_state.id, first_state.name))
