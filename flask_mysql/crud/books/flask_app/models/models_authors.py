from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_books

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name =  data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books=[]

# this method populates the home page with the list of authors (/authors)
    @classmethod
    def get_authors(cls):
        query = 'SELECT * FROM authors;'
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
        
# this method adds new author to the list on the homepage (/authors_add)
    @classmethod
    def add_authors(cls, data):
        query = 'INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('books_schema').query_db(query, data)

    #This method fills each authors' pages with books they liked (<int:author_id>)
    # This method gets one author with the books that s/he likes
    @classmethod
    def show_author(cls, data):
        query = 'SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;'
        results = connectToMySQL('books_schema').query_db(query, data)
        author = cls(results[0])
        for book in results:
            author.books.append(models_books.Book(book))
        return author