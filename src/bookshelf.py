from src.database import Book, Database
from src.search import search_keyword, search_details, book_info

db = Database()
session = db.session()

def search_booklist():
    keyword = input('Enter a search term: ')
    criteria = session.query(
        Book.id, Book.title).filter(
        Book.title.ilike('%' + keyword + '%')).all()
    output = [print(i[0], '-', i[1]) for i in criteria]
    return output

def search_bookshelf():
    if search_booklist():
        selection = input('Enter a number for book details: ')
        book_id = get_details(selection)
        selection = input('Change read count?: ').lower()
        if selection == 'yes':
            selection = input('New read count: ')
            reads(book_id, selection)

def get_details(book_id):
    selection = session.query(
        Book.title, Book.author, Book.read_count, Book.id).filter(
            Book.id == book_id).all()
    for detail in selection:
        print('\n')
        print('Title: ', detail[0])
        print('Author: ', detail[1])
        print('Read count: ', detail[2])
        print('\n')

        return detail[3]

def update_bookshelf():
    title, author = search_keyword()
    selection = input(
        'Please provide the number for the book you would like to add: '
    )
    selection = (int(selection) - 1)
    tree = search_details(author[selection], title[selection])
    title, author, read_count, gr_id, genres = book_info(tree)
    db.commit_to_db(session, title, author, read_count, gr_id, genres)

def reads(book, read_count):
    book_target = session.query(Book).filter(Book.id == book).first()
    book_target.read_count = read_count
