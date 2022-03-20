from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_users import User
from flask_app.models.model_recipes import Recipe

#login page
@app.route('/')
def index():
    return render_template('index.html')

#adding users to the login
@app.route('/add', methods = ['POST'])
def add_user():
    if not User.validate_register(request.form):
        return redirect('/')
    user_id = User.save_reg(request.form)
    session ['user_id'] = user_id
    return redirect('/dashboard')

# dashboard route to display the user name
@app.route('/dashboard')
def display():
    data = {
        'id': session['user_id']

    }
    return render_template('welcome.html', recipes = Recipe.get_all(), user = User.users_by_id(data))

@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    data ={
        'id':id
    }
    onerecipe = Recipe.get(data)
    data1={
        'id': session['user_id']
    }
    return render_template('recipes.html', user = User.users_by_id(data1), one_recipe=onerecipe)

@app.route('/recipes/new')
def add_recipe_page():
    current_user = session['user_id']
    print(current_user)
    return render_template('new.html', current_user = current_user)

@app.route('/recipes/new/add', methods = ['POST'])
def add_recipe():
    # data = {
        
    #     'name': request.form['name'],
    #     'date_made': request.form['date_made'],
    #     'description': request.form['description'],
    #     'under_30': request.form['under_30'],
    #     'instructions': request.form['instructions'],
    #     'user_id': request.form['user_id']

    # }
    if not Recipe.validate_info(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe_page(id):
    data= {
        'id': id
    }

    return render_template('edit.html', edit_recipe = Recipe.get(data))

@app.route('/recipes/updated', methods = ['POST'])
def edit_recipe():
    # data ={
    #     'id': request.form['id'],
    #     'name': request.form['name'],
    #     'date_made': request.form['date_made'],
    #     'description': request.form['description'],
    #     'under_30': request.form['under_30'],
    #     'instructions': request.form['instructions']
    # }
    if not Recipe.validate_info(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    print(data)
    Recipe.delete(data)
    return redirect('/dashboard')


@app.route('/login', methods = ['POST'])
def login():
    if not User.login_validation(request.form):
        return redirect('/')
    data ={
        'email': request.form['email']
    }
    user_db = User.users_by_email(data)
    session['user_id'] = user_db.id
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')