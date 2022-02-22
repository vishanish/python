from flask import Flask, render_template, request, redirect
# import the class from users.py
from users import User
app = Flask(__name__)

@app.route("/")
@app.route('/users')
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)

@app.route('/users/new')
def new_user():
    return render_template("new.html")

@app.route('/users/create', methods = ['POST'])
def create_user():
    User.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)