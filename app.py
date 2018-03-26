from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tname = "A"

#########

from datetime import datetime,date, timedelta
today = datetime.today()
lastmonth = today - timedelta(days=30)



from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import quandl

quandl.ApiConfig.api_key = 'usn6zz-R-PvDkbuLFbJ2'

# ticker_name = 'NFLX'

###########

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

# @app.route('/form')
# def form():
#   return render_template('form.html')

@app.route('/form', methods=['GET','POST'])
def my_form_post():
    if request.method == 'GET':
        print('if')
        # text = request.form['ticker']
        # tname = text.upper()
        # ticker_file= open("static/ticker.txt","w")
        # ticker_file.write(tname)
        # ticker_file.close()
        return render_template('form.html')
    else:
        text = request.form['ticker']
        tname = text.upper()
        ticker_file= open("static/ticker.txt","w")
        ticker_file.write(tname)
        ticker_file.close()
        # return plot()
        return render_template('form.html')
        # return render_template('form.html')
        # return 'POST' + tname

@app.route('/plot')
def plot():
    # text = request.form['ticker']
    # tname = text.upper()
    print('debug')
    f= open("static/ticker.txt","r")
    tname =f.read()
    f.close()
    # tname = request.form['ticker'].upper()
    print(tname)

    df = quandl.get_table('WIKI/PRICES', ticker= str(tname))
    myts = df[(df['date'] >= lastmonth) & (df['date'] < today)][['date','close']]

    plot = figure(x_axis_type="datetime", title="Stock Closing Prices "+ tname)
    plot.line(myts['date'], myts['close'])

    html_plot = file_html(plot, CDN, "my plot")
    Html_file= open("templates/plot.html","w")
    Html_file.write(html_plot)
    Html_file.close()
    return render_template('plot.html')




if __name__ == '__main__':
    app.run(port=33507)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
