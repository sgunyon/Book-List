from urllib.request import urlopen
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from organizer import Book, Details, Base

engine = create_engine('sqlite:////home/jill/Documents/Development/Python/sqlalchemy-workspace/BookList/test.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

api_key = 'Lu9ihra0oAJWLMkIcrDxw'
base_url = 'https://www.goodreads.com/search/index.xml?key='

def search():
    method = input('Search Booklist or New Books: ')

    if method == 'Booklist':
        search_booklist()
    elif method == 'New Books':
        search_new_by()
    else:
        print('Invalid search input')

def search_booklist():
    print('Search Booklist by: title, author, genre, or rereads')
    criteria = input('Enter search criteria: ')

    if criteria == 'title':
        print(session.query(Book.title).all())
    elif criteria == 'author':
        print(session.query(Details.author).all())
    elif criteria == 'genre':
        print(session.query(Details.genre).all())
    elif criteria == 'rereads':
        number = input('Number of rereads: ')
        print(session.query(Details).filter(Details.rereads==number))

search()

def search_new_by():
    print('Search fields: author or title')
    field = input('Enter search field: ')

    if field == 'author':
        search_by_author()
    elif field == 'title':
        search_by_title()
    else:
        print('Invalid search field')

def search_by_author():
    author = input('Enter an author: ')
    xml_string = (base_url + api_key + '&q=' + author.replace(' ', '%20'))
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)
    print('\n'.join([elem.text for elem in tree.iter(tag='title')]))


def search_by_title():
    title = input('Enter a title: ')
    xml_string = (base_url + api_key + '&q=' + title.replace(' ', '%20'))
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)
    print('\n'.join([elem.text for elem in tree.iter(tag='title')]))

search_new_by()
