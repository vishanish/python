from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:rows>')
@app.route('/<int:rows>/<int:columns>')
@app.route('/<int:rows>/<int:columns>/<string:color1>/<string:color2>')
def hello_world(rows = 4, columns = 4, color1 = 'red', color2 = 'black'):
    return render_template('index.html', rows=rows, columns=columns, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)