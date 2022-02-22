from flask_app import app
from flask_app.models.models_authors import Author
from flask_app.models.models_books import Book
from flask import render_template, request, redirect
from flask_app.models.models_favorites import Favorite

#This route is for the index page population
@app.route('/')
@app.route('/authors')
def get_authors():
    authors = Author.get_authors()
    return render_template('authors.html', authors=authors)

#This route is for adding authors to the index page
@app.route('/authors_add', methods = ['POST'])
def add_authors():
    data ={
        'name':request.form['name']
    }
    Author.add_authors(data)
    return redirect('/authors')

#This route leads to each authors' page and their favorite books
@app.route('/authors/<int:author_id>')
def show_author(author_id):
    data ={
        'id': author_id
    }                                       
    return render_template('author_id.html', all_books = Book.get_books(), author = Author.show_author(data))


# This route leads to the page of books
@app.route('/books')
def get_books():
    books = Book.get_books()
    return render_template('books.html', books = books)

# This route adds books to the page of books
@app.route('/books_add', methods = ['POST'])
def add_books():
    data ={
        'title':request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.add_books(data)
    return redirect('/books')

# Thie route leads to each individual book pages and the authors that liked the book()
@app.route('/books/<int:book_id>')
def show_book(book_id):
    data ={
        'id': book_id
    }                                       
    return render_template('book_id.html', all_authors = Author.get_authors(), book = Book.show_book(data))

@app. route('/author/<int:author_id>', methods=['POST'])
def add_books_to_authors(author_id):
    data = {
        "book_id": request.form['book_id'],
        "author_id": author_id
    }
    Favorite.add_books_to_author(data)
    return redirect (f'/authors/{author_id}')

@app. route('/book/<int:book_id>', methods=['POST'])
def add_authors_to_books(book_id):
    data = {
        "author_id": request.form['author_id'],
        "book_id": book_id
    }
    Favorite.add_books_to_author(data)
    return redirect (f'/books/{book_id}')