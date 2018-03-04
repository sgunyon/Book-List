import xml.etree.ElementTree as ET
from urllib.request import urlopen

from database import Book, Details

SEARCH_URL = 'https://www.goodreads.com/search/index.xml?key='
DETAILS_URL = 'https://www.goodreads.com/book/title.xml?key='
API_KEY = 'API KEY'

def search_keyword():
    keyword = input('Enter a search term: ')
    xml_string = (SEARCH_URL + API_KEY + '&q=' + keyword.replace(' ', '%20'))
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)

    author_list = []
    title_list = []

    [author_list.append(author.text) for author in tree.iter(tag='name')]
    [title_list.append(title.text) for title in tree.iter(tag='title')]
    count = 1

    for keys in title_list:
        print(count, keys)
        count += 1

    return title_list, author_list

def get_details(author, title):
    xml_string = (
        DETAILS_URL + API_KEY +
        '&title=' + title.replace(' ', '%20') +
        '&author=' + author.replace(' ', '%20')
        )
    print(xml_string)
    xml_file = urlopen(xml_string)
    tree = ET.ElementTree(file=xml_file)

    return tree

def book_info(tree):
    book_title = tree.find('.//title')
    author = tree.find('.//name')
    genre = ""

    parent = tree.find('.//popular_shelves')
    valid_genres = [
        'fiction', 'classics', 'regency', 'victorian',
        'science-fiction', 'fantasy', 'paranormal'
        ]

    for child in parent:
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
