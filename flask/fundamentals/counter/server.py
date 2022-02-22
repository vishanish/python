from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    if 'counter' in session:
        session['counter']  = session['counter'] + 1
    else:
        session['counter'] = 1
    
    if 'visits' in session:
        session['visits']  = session['visits'] + 1
    else:
        session['visits'] = 1
    return render_template("index.html")

@app.route('/increment', methods = ['POST'])
def increment():
    num =1
    if request.form['number'].isnumeric():
        num = int(request.form['number']) - 1
    if 'counter' in session:
        session['counter']  = session['counter'] + num
    else:
        session['counter'] = num
    return redirect('/')

@app.route('/destroy_session')
def desion():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)