from database import Database
from api import Search
from query import Query

def main():
    db = Database()
    engine = db.engine

    selection = input('Search Bookshelf or Library: ').lower()

    if selection == 'bookshelf':
        print('Search Criteria: title, author, genre, rereads')
        criteria = input('Enter search criteria: ')
        retrieve = Query(engine)
        retrieve.search_booklist(criteria)
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
