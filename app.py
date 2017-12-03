from flask import Flask, render_template, make_response, json, url_for,jsonify, request
from datetime import datetime

#scripts built for this app
import analyze as analyze
import crawler as crawler
import reader as reader

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search/<hashtag>/')
def search(hashtag):
    crawler.initializeCrawler(hashtag)
    return render_template('complete.html', hashtag=hashtag)
    #return render_template('index.html', hashtag=hashtag)

@app.route('/results/<hashtag>/')
def results(hashtag):
    data = reader.mostActiveTweeters(hashtag)
    return render_template('querypage.html', data=data, hashtag=hashtag)

@app.route('/results/<hashtag>/<screen_name>/tweets/')
def userTweets(hashtag, screen_name):
    tweets = reader.getUserTweets(hashtag, screen_name)
    return render_template('tweets.html', tweets=tweets, publisher=screen_name, hashtag=hashtag)

# Used for debugging. Outputs raw JSON from query
@app.route('/access/<hashtag>/')
def access(hashtag):
    return reader.rawResponse(hashtag)

# Shows a dashboard of all databases twitter_
@app.route('/dashboard/')
def dashboard():
    collections = reader.tweetsDash()
    return render_template('tweetdashboard.html', collections=collections)

# Landing page for analytics tools
@app.route('/analytics/', methods = ['GET', 'POST'])
def analytics():
    if request.method == 'POST':
        data = request.form.getlist('hashtags')
        # Perform some analytics

        return render_template('analytics.html', hashtags=data)
    else:
        return "Wrong HTTP request"

# Used for drawing lexical graphs
@app.route("/simple.png")
def simple():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
