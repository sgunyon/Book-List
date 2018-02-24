from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import database
import search


class Query():
    def __init__(self, criteria, engine):
        self.criteria = criteria
        self.engine = engine

    def start_session(self, engine):
        # Bind the engine to the metadata of Base class so
        # declaratives can be accessed in db instance
        Base.metadata.bind = engine
        # Establishes all conversations with the database
        # Acts as a 'staging zone' for all objects loaded into the db session object
        DBsession = sessionmaker(bind=engine)
        session = DBsession()

    # Insert new book and details into the tables
    def commit_to_db(self, session,engine):
        title = input('Enter a title: ')
        author = input('Enter an author: ')
        number = int(input('Enter # of times read: '))
        new_search = Search(title, author)
        book, author, genre = new_search.book_info()
        new_book = Book(title = book)
        session.add(new_book)
        session.commit()

        new_details = Details(
                                author = author,
                                genre = genre,
                                number_of_rereads = number,
                                book = new_book
                                )
        session.add(new_details)
        session.commit()

    # Query database
    def search_booklist(self, session):
        print('Search Booklist by: title, author, genre, or rereads')
        #self.criteria = input('Enter search criteria: ')

        if self.criteria == 'title':
            print(session.query(Book.title).all())
        elif self.criteria == 'author':
            print(session.query(Details.author).all())
        elif self.criteria == 'genre':
            print(session.query(Details.genre).all())
        elif self.criteria == 'rereads':
            number = input('Number of rereads: ')
            print(session.query(Details).filter(Details.rereads==number))
