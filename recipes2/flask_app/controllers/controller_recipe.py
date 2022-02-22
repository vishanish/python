from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_login import Login
from flask_app.models.model_recipes import Recipe


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add_user():
    if not Login.validate_register(request.form):
        return redirect('/')
    user_id = Login.save_reg(request.form)
    session ['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/dashboard')
def display():
    data = {
        'id': session['user_id']

    }
    return render_template('welcome.html', this_user = Login.get_recipes_by_userid(data))
    # return render_template('welcome.html', user = Login.users_by_id(data), this_user = Login.get_recipes_by_userid(data))

@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    data ={
        'id':id
    }
    onerecipe = Recipe.get_one(data)
    return render_template('recipes.html', user = Login.users_by_id(data), one_recipe=onerecipe)

@app.route('/recipes/new')
def add_recipe_page():
    current_user = session['user_id']
    print(current_user)
    return render_template('new.html', current_user = current_user)

@app.route('/recipes/new/add/<int:id>', methods = ['POST'])
def add_recipe(id):
    data = {
        
        'user_id': id,
        'name': request.form['name'],
        'date_made': request.form['date_made'],
        'description': request.form['description'],
        'under_30': request.form['under_30'],
        'instructions': request.form['instructions']

    }
    if not Recipe.validate_info(request.form):
        return redirect('/recipes/new')
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe_page(id):
    data= {
        'id': id
    }

    return render_template('edit.html', edit_recipe = Recipe.get_one(data))

@app.route('/recipes/updated', methods = ['POST'])
def edit_recipe():
    data ={
        'id': request.form['id'],
        'name': request.form['name'],
        'date_made': request.form['date_made'],
        'description': request.form['description'],
        'under_30': request.form['under_30'],
        'instructions': request.form['instructions']
    }
    if not Recipe.validate_info(request.form):
        return redirect(f'/recipes/edit/{{edit_recipe.id}}')
    Recipe.update(data)
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
    data ={
        'email': request.form['email']
    }
    user_db = Login.users_by_email(data)
    
    if Login.login_validation(request.form):
        session['email'] = request.form['email']
        session['user_id'] = user_db.id
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')