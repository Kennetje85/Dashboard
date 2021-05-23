import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#import cdata.mysql as mod
import plotly.graph_objs as go
import mysql.connector
import plotly.express as px

connection = mysql.connector.connect(host="localhost",user="root",password="",database="test")

cur = connection.cursor()
df = pd.read_sql("SELECT klantnummer, COUNT(*) as id FROM klant", connection)

app_name = 'OPL Dashboard'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'OPL Dashboard'

x = ['maandag' , 'dinsdag']
trace = go.Bar(x=x, y=df.id, name='ShipName')




app.layout = html.Div(children=[html.H1("OPL Dashboard", style={'textAlign': 'center'}),
                                dcc.Graph(
                                    id='example-graph',
                                    figure={
                                        'data': [trace],
                                        'layout':
                                            go.Layout(title='OPL', barmode='stack')
                                    })
                                ], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)

