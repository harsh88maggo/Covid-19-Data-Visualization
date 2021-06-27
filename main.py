from flask import Flask, render_template
import json



import json

import plotly.io as pio

import plotly

#import chart_studio.plotly as py

import plotly.graph_objs as go

import matplotlib.pyplot as plt

import pandas as pd
import warnings
import plotly.express as px
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import urllib.request as req
req.urlretrieve("https://prsindia.org/covid-19/cases/download","Covid.csv")

#recovery
df = pd.read_csv("Covid.csv")
state=df
state['Date']=pd.to_datetime(state["Date"],format="%d/%m/%Y")
state=state[state["Region"]!= "World"]
state=state[state["Region"]!= "India"]
state_data=state[state['Date']==state['Date'].iloc[-1]].reset_index(drop=True).drop("S. No.",axis=1)
#import plotly.express as px
fig=px.bar(state, x='Region', y='Cured/Discharged', color='Cured/Discharged' )
fig

#agewise
df1 = pd.read_csv('static/input/AgeGroupDetails.csv')


labels = df1.AgeGroup
values = df1.TotalCases
# Create subplots: use 'domain' type for Pie subplot
fig1 = make_subplots(rows=1, cols=2, specs=[[{'type':'xy'}, {'type':'domain'}]])
fig1.add_trace(go.Bar(x=labels, y=values, name="bar",marker = dict(color = 'rgba(0, 174, 174, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = labels),
              1, 1)
fig1.add_trace(go.Pie(labels=labels, values=values, name="pie"),
              1, 2)


fig1.update_layout(
    title_text="Covid-19 Age group details ")
    # Add annotations in the center of the donut pies.

#region
df2 = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
fig2 = go.Figure(data=go.Choropleth(
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locationmode='geojson-id',
    locations=state_data['Region'],
    z=state_data['Active Cases'],

    autocolorscale=False,
    colorscale='Reds',
    marker_line_color='peachpuff',
    colorbar=dict(
        title={'text': "Active Cases"},

        thickness=15,
        len=0.35,
        bgcolor='rgba(255,255,255,0.6)',

        tick0=0,
        dtick=20000,

        xanchor='left',
        x=0.01,
        yanchor='bottom',
        y=0.05
    )
))
fig2.update_geos(
    visible=False,
    projection=dict(
        type='conic conformal',
        parallels=[12.472944444, 35.172805555556],
        rotation={'lat': 24, 'lon': 80}
    ),
    lonaxis={'range': [68, 98]},
    lataxis={'range': [6, 38]}
)
fig2.update_layout(
    title=dict(
        text="Active COVID-19 Cases in India ",
        xanchor='center',
        x=0.3,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    height=550,
    width=550
)



pio.write_html(fig2, file='region.html', auto_open=False)
pio.write_html(fig, file='recovery.html', auto_open=False)
pio.write_html(fig1, file='agewise.html', auto_open=False)

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about.html")
def hello1():
    return render_template('about.html')

@app.route("/contact.html")
def hello2():
    return render_template('contact.html')

@app.route("/quiz2.html")
def hello3():
    return render_template('quiz2.html')

@app.route("/stat.html")
def hello4():
    return render_template('stat.html')

@app.route("/ref.html")
def hello5():
    return render_template('ref.html')

@app.route("/index.html")
def hello6():
    return render_template('index.html')







app.run(debug=True)