from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_replica_session():
    engine = create_engine('postgresql://ubuntu:qwerty@123@localhost:5432/tracking', echo=False)
    Session = sessionmaker(engine)
    session: Session = Session()
    return session

def connect_master_session():
    engine = create_engine('postgresql://ubuntu:qwerty@123@localhost:5432/tracking', echo=False)
    Session = sessionmaker(engine)
    session: Session = Session()
    return session
