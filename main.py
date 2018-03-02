from database import Database
from api import Search
from query import Query

def main():
    db = Database()

    selection = input('Search Bookshelf or Library: ').lower()

    if selection == 'bookshelf':
        print('Search Criteria: title, author, genre, rereads')
        criteria = input('Enter search criteria: ')
        retrieve = Query(criteria, db.return_engine())
        session = Query(criteria, db.return_engine())
        retrieve.search_booklist(session.start_session(db.return_engine()))
    elif selection == 'library':
        criteria = input('Search by author or title?: ')
        search = Search()

        if criteria == 'author':
            search.search_by_author()
        elif criteria == 'title':
            search.search_by_title()
        else:
            print('Invalid search field')
    else:
        print('Invalid search method')

main()
