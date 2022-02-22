from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/guess', methods = ['POST'])
def create_user():
    num = "25"
    print(request.form)
    session['number'] = request.form['number']
    if session['number'] < num:
        return "too low"
    if session['number'] > num:
        return "too high"
    return "hello"

# @app.route("/return")
# def back():
#     return redirect('/')
    
# adding this method
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)