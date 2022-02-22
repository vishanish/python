from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods = ['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    if 'name' not in request.form or 'location' not in request.form  or 'language' not in request.form or 'instructor' not in request.form  or 'comment' not in request.form or 'rating' not in request.form:
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['instructor'] = request.form.getlist('instructor')
    session['comment'] = request.form['comment']
    session['rating'] = request.form['rating']
    return redirect("/final")	 
    
@app.route("/final")
def show_user():
    print("Showing the Survey Form")
    return render_template("final.html")

@app.route('/return')
def desion():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)