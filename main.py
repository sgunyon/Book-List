from database import Database
from search import search_keyword, search_booklist, get_details, book_info


def main():
    db = Database()
    session = db.session()

    selection = input('Search Bookshelf or Library?: ').lower()

    if selection == 'bookshelf':
        criteria = input(
            'Enter search criteria (title, author, genre, rereads): '
            ).lower()
        search_booklist(criteria, session)

    elif selection == 'library':
        search_dict = search_keyword()
        add = input(
            'Would you like to add any of these books to your bookshelf? (yes/no) '
            ).lower()
        if add == 'yes':
            selection = input(
                'Please provide the number for the book you would like to add: '
            )
            tree = get_details(search_dict[int(selection)])
            title, author, genre = book_info(tree)
            db.commit_to_db(session, title, author, genre)

    else:
        print('Invalid selection')

main()
