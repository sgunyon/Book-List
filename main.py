from database import Database
from search import search_keyword, search_booklist, get_details, book_info


def main():
    db = Database()
    session = db.session()
    selection = []

    while selection != 'exit':
        selection = input('Search Bookshelf or Library?: ').lower()

        if selection == 'bookshelf':
            selection = input(
                'Enter search criteria (title, author, genre, rereads): '
                ).lower()
            search_booklist(selection, session)

        elif selection == 'library':
            title, author = search_keyword()
            selection = input(
                'Would you like to add any of these books to your bookshelf? (yes/no) '
                ).lower()
            if selection == 'yes':
                selection = input(
                    'Please provide the number for the book you would like to add: '
                )
                selection = (int(selection) - 1)
                tree = get_details(author[selection], title[selection])
                title, author, genre = book_info(tree)
                db.commit_to_db(session, title, author, genre)
        elif selection != 'exit':
            print('Invalid selection')

main()
