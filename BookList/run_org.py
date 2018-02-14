from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.request import urlopen
import xml.etree.ElementTree as ET

from organizer import Book, Details, Base

# Bind the engine to the metadata of Base class so
# declaratives can be accessed in db instance
engine = create_engine('sqlite:////home/jill/Documents/Development/Python/sqlalchemy-workspace/BookList/test.db')
Base.metadata.bind = engine

# Establishes all conversations with the database
# Acts as a 'staging zone' for all objects loaded into the db session object
DBsession = sessionmaker(bind=engine)
session = DBsession()

api_key = 'Lu9ihra0oAJWLMkIcrDxw'
base_url = 'https://www.goodreads.com/book/title.xml?&key='

def book_info(title):
    xml_string = (base_url + api_key + '&title=' + title.replace(' ', '%20'))
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)
    book_title = tree.find('.//title')
    author = tree.find('.//name')
    genre = tree.find('.//shelf[@name]')

    return book_title.text, author.text, genre

book_info()

# Insert new book into table
def commit_to_db(title, number):
    book, author, genre = book_info(title)
    new_book = Book(title = book)
    session.add(new_book)
    session.commit()

    new_details = Details(
                            author = author,
                            genre = genre,
                            rereads = number,
                            book = new_book
                            )
    session.add(new_details)
    session.commit()

commit_to_db()
