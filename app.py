import reader as reader
import analyze as analyze

from flask import Flask, render_template, make_response
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('index.html')
    # return """<h1>Hello heroku</h1><p>It is currently</p>"""

@app.route('/query/')
def returnRecord():
    return reader.topFive()
    #return pprint.pprint(reader.query())
    #return render_template('querypage.html', )

@app.route('/populate/')
def populate():
    reader.populate()
    return

@app.route('/analyze')
def analyze():
    return analysis()

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
