from flask_app import app
from flask_app.controllers import controllers_books_favorites_authors

if __name__ == "__main__":
    app.run(debug=True, port=5001)