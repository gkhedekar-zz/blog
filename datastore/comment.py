from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datastore import Base

CommentStatusEnum = Enum('approved', 'unapproved', name='comment_status')

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Interger, primary_key=True)
    content = Column(String, nullable=False)
    status = Column(CommentStatusEnum, nullable=False)
    create_time = Column(DateTime)

    author = Column(Integer, ForeignKey('user.id'))
    post = Column(Integer, ForeignKey('post.id'))