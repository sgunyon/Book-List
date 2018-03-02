import os
import sqlite3
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Declaratives allows table, mapper, and class object to be defined in one definition
Base = declarative_base()

class Book(Base):
    """ Outlines the 'book' table """
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    detail = relationship('Details', back_populates='book')

class Details(Base):
    """ Outlines the 'details' table """
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True)
    author = Column(String(50))
    genre = Column(String(50))
    number_of_rereads = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='detail')

class Database():
    """ Database create or interaction """
    def __init__(self):
        """ Creates engine """
        self.engine = create_engine('sqlite:///database/test.db')
        """ Creates the database if it doesn't already exist """
        if not os.path.isfile('database/test.db'):
            conn = sqlite3.connect('database/test.db')
            # Populates the tables for a newly created database
            conn.close()
            Base.metadata.create_all(self.engine)
