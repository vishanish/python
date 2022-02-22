from flask_app import app
from flask import render_template, request ,redirect
from flask_app.models.models_email import Email

@app.route ('/')
def index():
    return render_template("index.html")

@app.route('/form', methods = ['POST'])
def add_email():
    if not Email.validate_user(request.form):
        return redirect('/')
    # print(data)
    Email.add_emails(request.form)
    return redirect('/success')

@app.route('/success')
def emails_added():
    emails = Email.show_emails()
    return render_template('emails_added.html', emails = emails)