from sqlalchemy.orm import sessionmaker

from api import Search
from database import Base, Book, Details


class Query():
    def __init__(self, engine):
        self.engine = engine
        Base.metadata.bind = engine
        # Establishes all conversations with the database
        # Acts as a 'staging zone' for all objects loaded into the db session object
        DBsession = sessionmaker(bind=engine)
        self.session = DBsession()

    def search_booklist(self, criteria):
        print('Search Booklist by: title, author, genre, or rereads')

        if criteria == 'title':
            print(self.session.query(Book.title).all())
        elif criteria == 'author':
            print(self.session.query(Details.author).all())
        elif criteria == 'genre':
            print(self.session.query(Details.genre).all())
        elif criteria == 'rereads':
            number = input('Number of rereads: ')
            print(self.session.query(Details).filter(Details.rereads == number))

    # Insert new book and details into the tables
    def commit_to_db(self):
        title = input('Enter a title: ')
        author = input('Enter an author: ')
        number = int(input('Enter # of times read: '))
        new_search = Search()
        book, author, genre = new_search.book_info()
        new_book = Book(title=book)
        self.session.add(new_book)
        self.session.commit()

        new_details = Details(
            author=author,
            genre=genre,
            number_of_rereads=number,
            book=new_book
            )
        self.session.add(new_details)
        self.session.commit()
