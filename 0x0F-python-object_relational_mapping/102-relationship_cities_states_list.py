#!/usr/bin/python3
"""Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    usa = session.query(City, State).filter(State.id == City.state_id)
    print(usa)
    for item in usa:
        print('{}: {} -> {}'.format(item[0].id, item[0].name, item[1].name))
