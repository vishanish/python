from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_user import User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add_user():
    if not User.validate_register(request.form):
        return redirect('/')
    user_id = User.save_reg(request.form)
    session ['user_id'] = user_id
    return redirect('/display')

@app.route('/display')
def display():
    data = {
        'id': session['user_id']
    }
    return render_template('welcome.html', user = User.users_by_id(data))

@app.route('/login', methods = ['POST'])
def login():
    if not User.login_validation(request.form):
        return redirect('/')
    data ={
        'email': request.form['email']
    }
    user_db = User.users_by_email(data)
    # session['email'] = request.form['email'] #Not to store anything in session other than id
    session['user_id'] = user_db.id
    return redirect('display')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')