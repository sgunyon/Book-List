from database import Book, Database
from sqlalchemy import *
from search import search_keyword, search_details, book_info

db = Database()
session = db.session()

def search_booklist():
    keyword = input('Enter a search term: ')
    criteria = session.query(
        Book.id, Book.title).filter(
        Book.title.ilike('%' + keyword + '%')).all()
    [print(i[0], '-', i[1]) for i in criteria]

def search_bookshelf():
    search_booklist()
    selection = input('Enter a number for book details: ')
    book_id = get_details(selection)
    selection = input('Change read count?: ').lower()
    if selection == 'yes':
        selection = input('New read count: ')
        reads(book_id, selection)

def get_details(book_id):
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

def update_bookshelf():
    title, author = search_keyword()
    selection = input(
        'Please provide the number for the book you would like to add: '
    )
    selection = (int(selection) - 1)
    tree = search_details(author[selection], title[selection])
    title, author, genre, read_count = book_info(tree)
    db.commit_to_db(session, title, author, genre, read_count)

def reads(book, read_count):
    book_target = session.query(Book).filter(Book.id == book).first()
    book_target.read_count = read_count
