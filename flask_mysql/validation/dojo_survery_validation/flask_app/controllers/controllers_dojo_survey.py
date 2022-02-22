from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.models_dojo_survey import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods = ['POST'])
def create_user():
    if not Dojo.dojo_validate(request.form):
        return redirect('/')
    Dojo.add_to_survey(request.form)
    return redirect('/final')
    
    # if 'name' not in request.form or 'location' not in request.form  or 'language' not in request.form or 'instructor' not in request.form  or 'comment' not in request.form or 'rating' not in request.form:
    #     return redirect('/')
    # session['name'] = request.form['name']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
    # session['instructor'] = request.form.getlist('instructor')
    # session['comment'] = request.form['comment']
    # session['rating'] = request.form['rating']
    # Dojo.add_to_survey(request.form)
    # return redirect("/final")	 
    
@app.route("/final")
def show_user():
    print("Showing the Survey Form")
    return render_template("final.html")

@app.route('/return')
def desion():
    session.clear()
    return redirect('/')