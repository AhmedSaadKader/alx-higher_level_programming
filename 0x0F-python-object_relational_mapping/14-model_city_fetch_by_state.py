#!/usr/bin/python3
""" Script that prints all City objects from the
database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(
        City, State.name).order_by(
            City.id).filter(
                State.id == City.state_id)
    for city in cities:
        print("{}: ({}) {}".format(city.name, city[0].id, city[0].name))
