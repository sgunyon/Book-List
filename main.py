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
        title, author = search_keyword()
        add = input(
            'Would you like to add any of these books to your bookshelf? (yes/no) '
            ).lower()
        if add == 'yes':
            selection = input(
                'Please provide the number for the book you would like to add: '
            )
            index = (int(selection) - 1)
            tree = get_details(author[index], title[index])
            title, author, genre = book_info(tree)
            db.commit_to_db(session, title, author, genre)

    else:
        print('Invalid selection')

main()
