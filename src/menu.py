import os
import sys

from src.search import search_keyword
from src.bookshelf import search_bookshelf, update_bookshelf


menu_action = {}

def main_menu():
    os.system('clear')

    print('\n MAIN MENU')
    print('b : Bookshelf')
    print('l : Library')
    print('q : Quit')
    option = input('Select an option >> ')
    exec_menu(option)

    return

def exec_menu(option):
    os.system('clear')
    op = option.lower()
    if op == '':
        menu_action['main_menu']()
    else:
        try:
            menu_action[op]()
            #option = input('Select an option >> ')
        except KeyError:
            print('Invalid Selection!')
        menu_action['main_menu']()

def bookshelf_menu():
    print('\n Bookshelf Menu')
    print('s : Search')
    print('r : Return to main menu')
    option = input('Select an option: ')
    exec_menu(option)

    return option

def library_menu():
    print('\n Library Menu')
    print('c : Search')
    print('u : Update Bookshelf')
    print('r : Return to main menu')
    print('q : Quit')
    option = input('Select an option: ')
    exec_menu(option)

    return option

def back():
    menu_action['menu_menu']()

def exit():
    sys.exit()

menu_action = {
    'main_menu': main_menu,
    'b' : bookshelf_menu,
    'l' : library_menu,
    's' : search_bookshelf,
    'c' : search_keyword,
    'u' : update_bookshelf,
    'r' : back,
    'q' : exit
}

if __name__ == '__main__':
    main_menu()
