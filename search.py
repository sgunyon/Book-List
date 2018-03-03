import xml.etree.ElementTree as ET
from urllib.request import urlopen

from database import Book, Details

API_KEY = 'Lu9ihra0oAJWLMkIcrDxw'
BASE_URL = 'https://www.goodreads.com/search/index.xml?key='

def search_keyword():
    keyword = input('Enter a search term: ')
    xml_string = (BASE_URL + API_KEY + '&q=' + keyword.replace(' ', '%20'))
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)

    result_dict = {}
    count = 0

    for elem in tree.iter(tag='title'):
        result_dict[count] = elem.text
        print(count, result_dict[count])
        count += 1

    return result_dict

def get_tree(title):
    xml_string = (BASE_URL + API_KEY + '&title=' + title.replace(' ', '%20'))
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)

    return tree

def book_info(tree):
    book_title = tree.find('.//title')
    author = tree.find('.//name')

    parent = tree.find('.//popular_shelves')
    valid_genres = [
        'fiction', 'classics', 'regency', 'victorian',
        'science-fiction', 'fantasy', 'paranormal'
        ]

    for child in parent:
        genre = child.get('name')
        if child.get('name') in valid_genres:
            genre = child.get('name')
            break
        else:
            continue

    return book_title.text, author.text, genre

def search_booklist(criteria, session):
    if criteria == 'title':
        print(session.query(Book.title).all())
    elif criteria == 'author':
        print(session.query(Details.author).all())
    elif criteria == 'genre':
        print(session.query(Details.genre).all())
    elif criteria == 'rereads':
        number = input('Number of rereads: ')
        print(session.query(Details).filter(Details.rereads == number))
