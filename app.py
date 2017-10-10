import reader

from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('index.html')
    # return """<h1>Hello heroku</h1><p>It is currently</p>"""

@app.route('/query/')
def query():
    # return pprint.pprint(reader.query())
    return query()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
