from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    <p>It is currently</p>

    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
