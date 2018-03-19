from database import Database
from search import search_keyword, search_details, book_info
from bookshelf import search_booklist, get_details, update_reads


def main():
    db = Database()
    session = db.session()
    selection = []

    print('\n###########################################')
    print('#  Welcome to the Goodreads Book Manager  #')
    print('###########################################')

    while selection != 'exit':
        selection = input('\nSearch Bookshelf or Library?: ').lower()

        if selection == 'bookshelf':
            search_booklist(session)
            selection = input('\nEnter a number for book details: ')
            book_id = get_details(session, selection)
            selection = input('\nChange read count?: ').lower()
            if selection == 'yes':
                selection = input('\nNew read count: ')
                update_reads(session, book_id, selection)

        elif selection == 'library':
            title, author = search_keyword()
            selection = input(
                '\nWould you like to add any of these books to your bookshelf? (yes/no) '
                ).lower()
            if selection == 'yes':
                selection = input(
                    '\nPlease provide the number for the book you would like to add: '
                )
                selection = (int(selection) - 1)
                tree = search_details(author[selection], title[selection])
                title, author, genre, read_count = book_info(tree)
                db.commit_to_db(session, title, author, genre, read_count)

        elif selection != 'exit':
            print('Invalid selection')

main()
