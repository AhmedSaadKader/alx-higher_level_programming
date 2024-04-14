#!/usr/bin/python3
""" Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine, select
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    with engine.connect() as con:
        s = select(State).order_by(State.id).filter(State.name == sys.argv[4])
        result = con.execute(s)
        first_state = result.first()
        if first_state is None:
            print("Not found")
        else:
            print('{}'.format(first_state.id))
