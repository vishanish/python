from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello world!')

@app.route('/dojo')
def dojo():
    return('dojo')

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return(f'Hi {name}')

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    print(num)
    print(word)
    return(f'Hi {word * num}')

@app.errorhandler(404)
def page_not_found(error):
    return('Page not found'),404

if __name__ == "__main__":
    app.run(debug=True)
