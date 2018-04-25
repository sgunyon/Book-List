# Bookbag
An application to search Goodreads and store books in a local database.

### Dependencies
- Python3
- sqlalchemy
- sqlite3
- flask

### Goodreads API key
You will need to register with Goodreads and obtain an API key to use this program. You can do so using this link:

- https://www.goodreads.com/api

Once you have your api key, you will need to create a file in the src directory called api.py and add your api key as a variable like so:

`HIDDEN_KEY = 'YOUR API KEY HERE'`

### Usage
This application has both graphical and terminal interfaces.
To launch the terminal interface:

`python src/menu.py`

To launch the flask app:

`python app.py`

### Tips

Generally, the term bookshelf refers to your local database with the options to search or update books you are cataloging locally.

Library searches Goodreads for book suggestions, and provides an interface for adding books to your personal bookshelf.
