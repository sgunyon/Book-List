from database import Book
from sqlalchemy import *

def search_booklist(session):
    keyword = input('Enter a search term: ')
    criteria = session.query(
        Book.id, Book.title).filter(
        Book.title.ilike('%' + keyword + '%')).all()
    [print(i[0], '-', i[1]) for i in criteria]

def get_details(session, book_id):
    selection = session.query(
        Book.title, Book.author, Book.genre, Book.read_count, Book.id).filter(
            Book.id == book_id).all()
    for detail in selection:
        print('\n')
        print('Title: ', detail[0])
        print('Author: ', detail[1])
        print('Genre: ', detail[2])
        print('Read count: ', detail[3])
        print('\n')

        return detail[4]

def reads(session, book, read_count):
    book_target = session.query(Book).filter(Book.id == book).first()
    book_target.read_count = read_count
