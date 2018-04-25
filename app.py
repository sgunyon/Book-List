import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

from src.database import Database, Book, Genre
from src.search import search_keyword
from src.bookshelf import search_bookshelf, update_bookshelf

db = Database()
session = db.session()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form.get("view"):
        # selection = request.form.get("view")
        books = session.query(Book.id, Book.title)
        return render_template("search_bookshelf.html", books=books)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
