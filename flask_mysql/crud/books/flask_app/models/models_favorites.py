from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self,data):
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_id = data[['author_id']]
        self.book_id = data ['book_id']
    
    @classmethod
    def add_books_to_author(cls, data):
        query = 'INSERT INTO favorites (created_at, updated_at, author_id, book_id) VALUES (NOW(), NOW(), %(author_id)s, %(book_id)s);'
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def add_authors_to_book(cls, data):
        query = 'INSERT INTO favorites (created_at, updated_at, author_id, book_id) VALUES (NOW(), NOW(), %(author_id)s, %(book_id)s);'
        return connectToMySQL('books_schema').query_db(query, data)
        