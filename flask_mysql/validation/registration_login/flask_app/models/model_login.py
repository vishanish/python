from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
bcrypt = Bcrypt(app)

class Login:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_reg(cls,data):
        pass_hash = bcrypt.generate_password_hash(data['password'])
        user ={
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': pass_hash
        }
        query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        return connectToMySQL('users_schema').query_db(query, user)

    
    @classmethod
    def login_validation(cls, data):
        registered_user = Login.users_by_email(data) 
        if not registered_user:
            flash("Invalid Email/Password")
            return False
        if not bcrypt.check_password_hash(registered_user.password, data['password']):
            flash("Invalid Email/Password")
            return False
        return True


    @classmethod
    def users_by_email(cls, data):
        query ='SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('users_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def users_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash('First name needs to be atleast 3 characters long', 'registration')
            is_valid = False
        if len(data['last_name']) < 3:
            flash('Last name needs to be atleast 3 characters long', 'registration')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Email address is not valid!", 'registration')
            is_valid = False
        if len(data['email']) < 1:
            flash('Email cannot be empty', 'registration')
            is_valid = False
        if len(data['password']) < 3:
            flash('Password needs to atleast 3 characters long', 'registration')
            is_valid = False
        if (data['confirm'] != data['password']):
            flash('Your passwords do not match', 'registration')
            is_valid = False
        return is_valid