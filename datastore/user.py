from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datastore import Base

class User(Base):
	__tablename__ = 'user'

	id = Column(Interger, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    posts = relationship('Post', backref='user', cascade='all, delete-orphan')