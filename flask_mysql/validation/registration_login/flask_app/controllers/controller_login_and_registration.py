from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_login import Login


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add_user():
    if not Login.validate_register(request.form):
        return redirect('/')
    user_id = Login.save_reg(request.form)
    session ['user_id'] = user_id
    return redirect('/display')

@app.route('/display')
def display():
    data = {
        'id': session['user_id']
    }
    return render_template('welcome.html', user = Login.users_by_id(data))

@app.route('/login', methods = ['POST'])
def login():
    data ={
        'email': request.form['email']
    }
    user_db = Login.users_by_email(data)
    
    if Login.login_validation(request.form):
        session['email'] = request.form['email']
        session['user_id'] = user_db.id
        return redirect('display')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')