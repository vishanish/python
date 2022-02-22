from flask import render_template, redirect, request
from flask_app.models.users import User
from flask_app import app

@app.route("/")
@app.route('/users')
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)
# add a user button on hompeage calls the html page new.html
@app.route('/users/new')
def new_users():
    return render_template('new.html')
# create a user button on new.html page calls this function to post the data to the database
# WIP: need to ge the redirect to the individual page of the user
@app.route('/users/create', methods=["POST"])
def create_user():
    userid =User.create(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect(f'/users/{userid}')
# WIP: need to populate the user.html page with the user info
@app.route('/users/<int:userid>')
def show_user(userid):
    data ={
        'id':userid
    }
    oneuser = User.get_one(data)
    return render_template('user.html', one_user=oneuser)
# WIP: edit button on the home page should render_template for the individual user
@app.route('/users/<int:id>/edit')
def user_edit(id):
    data = {
        'id':id
    }
    return render_template('edit.html', one_user=User.get_one(data))
#WIP: the update user button on the edit page show update the date on the database
@app.route('/user/<int:userid>/update', methods = ['POST'])
def update_user(userid):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': userid
    }
    User.update(data)
    return redirect(f'/users/{userid}')