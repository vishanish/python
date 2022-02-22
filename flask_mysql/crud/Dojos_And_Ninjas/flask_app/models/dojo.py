from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        if results:
            for dojo in results:
                dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        
    @classmethod
    def show_dojos(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id =%(id)s'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            dojo.ninjas.append(Ninja(row))
        return dojo
    
    