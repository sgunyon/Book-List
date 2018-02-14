#!/usr/bin/python

import sys
import os
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Declaratives allows table, mapper, and class object to be defined in one definition
Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key = True)
    title = Column(String(255), nullable = False)
    detail = relationship('Details', back_populates='book')

class Details(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key = True)
    author = Column(String(50))
    genre = Column(String(50))
    rereads = Column(Integer, nullable = False)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='detail')

# Stores data in the local directory
engine = create_engine('sqlite:////home/jill/Documents/Development/Python/sqlalchemy-workspace/BookList/test.db')
# Creates all tables in the engine
Base.metadata.create_all(engine)
