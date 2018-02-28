from database import Database
from api import Search
from query import Query

def search():
    method = input('Search Booklist or New Books: ')

    if method == 'Booklist':
        print('Search Criteria: title, author, genre, rereads')
        criteria = input('Enter search criteria: ')
        db = Database()
        retrieve = Query(criteria, db.return_engine())
        session = Query(criteria, db.return_engine())
        retrieve.search_booklist(session.start_session(db.return_engine()))
    elif method == 'New Books':
        search_for_suggestions()
    else:
        print('Invalid search method')

# Search GoodReads for book suggestions
def search_for_suggestions():
    print('Search fields: author or title')
    field = input('Enter search field: ')

    if field == 'author':
        new_search = Search(author)
        new_search.search_by_author()
    elif field == 'title':
        new_search = Search(title)
        new_search.search_by_title()
    else:
        print('Invalid search field')


search()
