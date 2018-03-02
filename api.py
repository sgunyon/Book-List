from urllib.request import urlopen
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import database


api_key = 'Lu9ihra0oAJWLMkIcrDxw'
base_url = 'https://www.goodreads.com/search/index.xml?key='

class Search():
    def __init__(self):
        pass

    def api_call_title(self):
        action = input('Enter action (search or add): ')
        title = input('Enter a title: ')

        if action == 'search':
            xml_string = (base_url + api_key + '&q=' + title.replace(' ', '%20'))
        elif action == 'add':
            xml_string = (base_url + api_key + '&title=' + title.replace(' ', '%20'))

        xml_file = urlopen(xml_string)
        tree = ET.ElementTree(file=xml_file)

        return tree

    def api_call_author(self):
        author = input('Enter an author: ')
        xml_string = (base_url + api_key + '&q=' + author.replace(' ', '%20'))
        xml_file = urlopen(xml_string)
        tree = ET.ElementTree(file=xml_file)

        return tree

    def book_info(self):
        tree = self.api_call_title()
        book_title = tree.find('.//title')
        author = tree.find('.//name')

        parent = tree.find('.//popular_shelves')
        valid_genres = ['fiction', 'classics', 'regency', 'victorian', 'science-fiction', 'fantasy', 'paranormal']

        for child in parent:
            genre = child.get('name')
            if child.get('name') in valid_genres:
                genre = child.get('name')
                break
            else:
                continue

        return book_title.text, author.text, genre

    def search_by_author(self):
        tree = self.api_call_author()
        print('\n'.join([elem.text for elem in tree.iter(tag='title')]))

    def search_by_title(self):
        tree = self.api_call_title()
        print('\n'.join([elem.text for elem in tree.iter(tag='title')]))
