from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data ['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def show_emails(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL('email_schema').query_db(query)
        emails =[]
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def add_emails(cls, data):
        # print(data)
        query = 'INSERT INTO emails(email, created_at, updated_at)VALUES(%(email)s, NOW(), NOW());'
        return connectToMySQL('email_schema').query_db(query,data)

    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Email address is not valid!", 'login')
            is_valid = False
        if len(user['email']) < 1:
            flash('Email cannot be empty', 'login')
            is_valid = False
        flash('The email address you entered is valid', 'success')
        return is_valid