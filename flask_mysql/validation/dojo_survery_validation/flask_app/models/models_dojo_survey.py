from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.instructor = data['instructor']
        self.comment = data['comment']
        self.rating = data['rating']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def add_to_survey(cls, data):
        query = 'INSERT INTO dojos (name, location, language, instructor, comment, rating, created_at, updated_at)VALUES(%(name)s, %(location)s, %(language)s, %(instructor)s, %(comment)s, %(rating)s, NOW(), NOW())'
        return connectToMySQL('dojo_survery_schema').query_db(query, data)
    
    @staticmethod
    def dojo_validate(data):
        is_valid = True
        if len(data['name']) < 1:
            flash('Need the name', 'name')
            is_valid = False
        if len(data['location']) < 1:
            flash('Need to select Dojo Location', 'location')
            is_valid = False
        if len(data['language']) < 1:
            flash('Need to select a language', 'language')
            is_valid = False
        # if len(data['instructor']) == 1:
        #     flash('Need to select your favorite instructor', 'instructor')
        #     is_valid = False
        if len(data['comment']) < 1:
            flash('Need to add a comment', 'comment')
            is_valid = False
        # if len(data['rating']) < 0:
        #     flash('Need to rate your experience', 'rating')
        #     is_valid = False
        return is_valid