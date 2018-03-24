import os
import sqlite3
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# Declaratives allows table, mapper, and class object to be defined in one definition
BASE = declarative_base()

book_genres = Table('book_genres', BASE.metadata,
                    Column('book_id', Integer, ForeignKey('book.id')),
                    Column('genre_id', Integer, ForeignKey('genre.id'))
                   )

class Book(BASE):
    """ Outlines the 'book' table """
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(50))
    read_count = Column(Integer)
    good_reads_id = Column(Integer)
    genres = relationship("Genre", backref="book", secondary=book_genres)


class Genre(BASE):
    """ Outlines the 'genre' table """
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    genre = Column(String(255), nullable=False)


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
    def commit_to_db(self, session, title, author, read_count, gr_id, genres):
        new_book = Book(
            title=title,
            author=author,
            read_count=read_count,
            good_reads_id=gr_id
            )

        new_book.genres = [Genre(genre=genre) for genre in genres]

        session.add(new_book)
        session.commit()
