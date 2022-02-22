from flask_app import app
from flask_app.controlllers import controllers_email

if __name__ == "__main__":
    app.run(debug=True, port=5001)