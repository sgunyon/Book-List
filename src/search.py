import xml.etree.ElementTree as ET
from urllib.request import urlopen

from src.api import HIDDEN_KEY

SEARCH_URL = 'https://www.goodreads.com/search/index.xml?key='
DETAILS_URL = 'https://www.goodreads.com/book/title.xml?key='
API_KEY = HIDDEN_KEY


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

def search_details(author, title):
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
    gr_id = tree.find('.//id')
    genres = {}
    read_count = 0

    parent = tree.find('.//popular_shelves')

    for child in parent:
        genres[child.get('name')] = child.get('count')

    return book_title.text, author.text, read_count, gr_id.text, genres
