import os
import sqlite3
from sqlalchemy import Column, String, Integer, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Declaratives allows table, mapper, and class object to be defined in one definition
BASE = declarative_base()

class Book(BASE):
    """ Outlines the 'book' table """
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(50))
    genre = Column(PickleType)
    read_count = Column(Integer())

class Database():
    """ Database create or interaction """
    def __init__(self):
        """ Creates engine """
        self.engine = create_engine('sqlite:///database/test.db')
        """ Creates the database if it doesn't already exist """
        if not os.path.exists('database'):
            os.makedirs('database')
        if not os.path.isfile('database/test.db'):
            conn = sqlite3.connect('database/test.db')
            # Populates the tables for a newly created database
            conn.close()
            BASE.metadata.create_all(self.engine)

    def session(self):
        BASE.metadata.bind = self.engine
        # Establishes all conversations with the database
        # Acts as a 'staging zone' for all objects loaded into the db session object
        DBsession = sessionmaker(bind=self.engine)
        session = DBsession()
        return session

    # Insert new book and details into the tables
    def commit_to_db(self, session, title, author, genre, read_count):
        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            read_count=read_count,
            )
        session.add(new_book)
        session.commit()
