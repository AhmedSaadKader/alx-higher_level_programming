#!/usr/bin/python3
""" Script that prints the first State object from
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import select, create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    s = session.query(State).order_by(State.id).filter(
        State.name.like('%a%'))
    for row in s:
        print('{}: {}'.format(row.id, row.name))
