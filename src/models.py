import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    phone_number = Column(String(25))

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(5000), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    tags = Column(String(2500))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    media_type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user = relationship(User)

class Tag(Base):
    __tablename__ = 'tag'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(250), nullable=False)
    user = relationship(User)

class Post_tag(Base):
    __tablename__ = 'post_tag'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    tag_from_id = Column(Integer, ForeignKey('tag.id'), nullable=False)
    post_to_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e