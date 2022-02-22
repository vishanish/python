from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.dojo import Dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def save_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id)' \
            'VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_ninjas(cls, data):
        query = 'SELECT * FROM ninjas WHERE dojo_id = %(id)s'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

