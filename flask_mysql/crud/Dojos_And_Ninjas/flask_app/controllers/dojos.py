from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
@app.route('/dojos')
def index(): # populates the homepage with the list of all the provided dojos
    dojos = Dojo.get_all_dojos()  # calls the method get_all_dojos from the Dojo class in the dojo model and adds the dojos the dojo variable
    print(dojos)
    return render_template('dojo.html', all_dojos=dojos) 

# adds the new dojo to the homepage 
@app.route('/dojos/add', methods = ['POST'])
def dojos_add():
    data = {
        'name': request.form['name']
    }
    Dojo.save_dojo(data) #calls the method save_dojo from the Dojo class in the dojo model in the dojo
    return redirect('/')

# populates the dojo_show template with Dojo Name, Ninjas associated with the Dojo, and provides id in the URL
@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id): #gets the dojo_id from the URL 
    data ={
        'id': dojo_id
    }                                       #add the dojo id to the URL and the name of the dojo to the page
    return render_template('dojo_show.html', dojo = Dojo.show_dojos(data), ninjas = Ninja.get_ninjas(data))
                                                                            #add the list of ninja associated with the dojo