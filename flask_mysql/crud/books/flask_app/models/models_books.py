from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_authors

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title =  data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors =[]
    
    #This method get the books and populates the page for books(/books)
    @classmethod
    def get_books(cls):
        query = 'SELECT * FROM books;'
        results = connectToMySQL('books_schema').query_db(query)
        books=[]
        for book in results:
            books.append(cls(book))
        return books
    
    #This method adds books to the list on the page of books(/books_add)
    @classmethod
    def add_books(cls, data):
        query = 'INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());'
        return connectToMySQL('books_schema').query_db(query, data)
    
#This method fills each books' pages with authors that liked the book (<int:book_id>)
#This method is to get one book with the list of authors that liked the book
    @classmethod
    def show_book(cls, data):
        query = 'SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;'
        results = connectToMySQL('books_schema').query_db(query, data)
        book = cls(results[0])
        for author in results:
            book.authors.append(models_authors.Author(author))
        return book