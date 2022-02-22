from flask_app import app
from flask_app.controllers import controller_login_and_registration

if __name__ == "__main__":
    app.run(debug=True, port=5001)