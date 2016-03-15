from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datastore import Base

PostStatusEnum = Enum('draft', 'published', 'outdated', name='post_status')

class Post(Base):
    __tablename__ = 'post'

    id = Column(Interger, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    status = Column(PostStatusEnum, nullable=False)
    create_time = Column(DateTime)
    update_time = Column(DateTime)

    author = Column(Integer, ForeignKey('user.id'))
    comments = relationship('Comment', backref='post', cascade='all, delete-orphan')

