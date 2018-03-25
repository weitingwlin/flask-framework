from flask import Flask, render_template, request, redirect

app = Flask(__name__)

ticker = 'A'

#########
# import quandl
# from datetime import datetime,date, timedelta
# today = datetime.today()
# lastmonth = today - timedelta(days=30)
#
# quandl.ApiConfig.api_key = 'usn6zz-R-PvDkbuLFbJ2'
# df = quandl.get_table('WIKI/PRICES', ticker='A')
#
# myts = df[(df['date'] >= lastmonth) & (df['date'] < today)][['date','close']]

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = figure()
# plot.circle(myts['date'], myts['close'])
plot.circle([1,2], [3.4])

html_plot = file_html(plot, CDN, "my plot")
Html_file= open("templates/plot.html","w")
Html_file.write(html_plot)
Html_file.close()
###########

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/form')
def form():
  return render_template('form.html')

@app.route('/plot')
def plot():
  return render_template('plot.html')

if __name__ == '__main__':
  app.run(port=33507)
