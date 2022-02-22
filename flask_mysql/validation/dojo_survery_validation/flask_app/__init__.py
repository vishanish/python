from flask import Flask, flash

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'