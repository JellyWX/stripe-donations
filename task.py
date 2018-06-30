from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SimpleUser(Base):
    id = Column( Integer, primary_key=True)
    username = Column( String )
    email = Column( String, index=True, unique=True)
    user_id = Column( BigInteger, unique=True)
    subscriptions = Column( String )

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
