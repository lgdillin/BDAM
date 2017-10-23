from flask import Flask, render_template, make_response, json, url_for
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
    data = reader.topFive(hashtag)
    return render_template('querypage.html', data=data)
    #return render_template('index.html', hashtag=hashtag)

@app.route('/query/')
def returnResults():
    hashtag='BREAKING'
    data = reader.topFive(hashtag)
    return render_template('querypage.html', data=data)

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
