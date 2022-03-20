from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.desciprtion = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipes (name, under_30, instructions, date_made, created_at, updated_at, user_id)' \
            'VALUES (%(name)s, %(under_30)s, %(instructions)s, %(date_made)s, NOW(), NOW(), %(user_id)s);'
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, under_30 = %(under_30)s,' \
            'instructions = %(instructions)s, date_made =  %(date_made)s, updated_at =  NOW() WHERE id = %(id)s;'
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    

    @staticmethod
    def validate_info(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Name needs to be atleast 3 characters long')
            is_valid = False
        if 'under_30' not in data:
            flash('Need to show if under or over 30')
            is_valid = False
        if len(data['instructions']) < 10:
            flash('Instuctions need to be atleaset 10 characters long')
            is_valid = False
        if len(data['description']) < 10:
            flash('Description need to be atleaset 10 characters long')
            is_valid = False
        if data ['date_made'] == "":
            flash('Need to enter a date')
            is_valid = False
        return is_valid