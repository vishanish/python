from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojol = Dojo.get_all_dojos() # get the list of dojos and populates the drop down in the create ninja html
    print(dojol)
    return render_template('ninja.html', all_dojol=dojol)


@app.route('/ninjas/add', methods = ['POST'])
def ninjas_add():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.save_ninja(data)
    return redirect('/')
