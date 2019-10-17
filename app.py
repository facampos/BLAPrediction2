#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:54:55 2019

@author: fabiocampos
"""

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("assig6.csv", sep=",")
X = df[df.columns.difference(['Paper 7', 'pair', 'id', 'sem' ])]
Y=df['Paper 7']

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

regressor = LinearRegression()  
regressor.fit(X_train, Y_train) 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

app.layout = html.Div([
        
    html.H1('Paper 7`s Magic Oracle'),
        
    html.Div([   
    html.Label('Paper 1'),
    dcc.Slider(id='p1',
            min=0, max=100, step=5, value=0,
               marks={
        0: {'label': '0'},
        25: {'label': '25'},
        100: {'label': '100'},
        50: {'label': '50'},
        75: {'label': '75'}                                
    }),

    html.Div([   
    html.Label('Paper 2'),
    dcc.Slider(id='p2',
            min=0, max=100, step=5, value=0,
               marks={
        0: {'label': '0'},
        25: {'label': '25'},
        100: {'label': '100'},
        50: {'label': '50'},
        75: {'label': '75'}                                
    }),
]),

    html.Div([   
    html.Label('Paper 3'),
    dcc.Slider(id='p3',
            min=0, max=100, step=5, value=0,
               marks={
        0: {'label': '0'},
        25: {'label': '25'},
        100: {'label': '100'},
        50: {'label': '50'},
        75: {'label': '75'}                                
    }),
]),

    html.Div([   
    html.Label('Paper 4'),
    dcc.Slider(id='p4',
            min=0, max=100, step=5, value=0,
               marks={
        0: {'label': '0'},
        25: {'label': '25'},
        100: {'label': '100'},
        50: {'label': '50'},
        75: {'label': '75'}                                
    }),
]),

    html.Div([   
    html.Label('Paper 5'),
    dcc.Slider(id='p5',
            min=0, max=100, step=5, value=0,
               marks={
        0: {'label': '0'},
        25: {'label': '25'},
        100: {'label': '100'},
        50: {'label': '50'},
        75: {'label': '75'}                                
    }),
]),

    html.Div([   
    html.Label('Paper 6'),
    dcc.Slider(id='p6',
            min=0, max=100, step=5, value=0,
               marks={
        0: {'label': '0'},
        25: {'label': '25'},
        100: {'label': '100'},
        50: {'label': '50'},
        75: {'label': '75'}                                
    }),
]),

],className="pretty_container four columns"),

  html.Div([ 

    daq.Thermometer(
        id='my-gauge',
        showCurrentValue=True,
#color={"gradient":True,"ranges":{"red":[0,40],"yellow":[41,68],"green":[68.1,100]}},
        label="Will Paper 7 be healthy?",
        max=100,
        min=0,
        value=60
    ),
])
    ])


@app.callback(
    Output('my-gauge', 'value'),
    [Input('p1', 'value'),
     Input('p2', 'value'),
     Input('p3', 'value'),
     Input('p4', 'value'),
     Input('p5', 'value'),
     Input('p6', 'value'),
     ])
def update_output_div(pa1,
                      pa2,
                      pa3,
                      pa4,
                      pa5,
                      pa6):
   X_case =pd.DataFrame({'Paper 1':[pa1],'Paper 2':[pa2],'Paper 3':[pa3],'Paper 4':[pa4],'Paper 5':[pa5],'Paper 6':[pa6]})
   Y_case = regressor.predict(X_case)
   return Y_case[0]

if __name__ == '__main__':
    app.run_server()
