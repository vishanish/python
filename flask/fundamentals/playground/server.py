from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:times>')
@app.route('/play/<int:times>/<string:color>')
def color(times = 3, color = 'blue'):
    return render_template('index.html', times = times, color = color)

if __name__=='__main__':
    app.run(debug=True)
