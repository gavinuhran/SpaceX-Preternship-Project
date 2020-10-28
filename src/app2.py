# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.io as pio
import pandas as pd
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'include'))

from init_data import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

weights = [1,1,1,1,1]

data = import_data("FakeData", weights)

scores = []
for vendor in data.keys():
    val = data[vendor].get_score()
    val = val * 100
    scores.append(val)

scores_dict = {'Vendor_Name' : list(data.keys()), 'Vendor_Scores' : scores}

fig = px.bar(scores_dict, x='Vendor_Name', y = 'Vendor_Scores')

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


def generate_table():
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in list(scores_dict.keys())])
        ),
        html.Tbody([
            html.Tr([
                html.Td(data[name].name),
                html.Td(scores[i])
            ])for i, name in enumerate(list(data.keys()))
        ])
    ])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='SpaceX Preternship Projet',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Vendor Analysis based on their previous performance', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='Vendor_Scores',
        figure = fig
    ),

    generate_table()
])

if __name__ == '__main__':
    app.run_server(debug=True)
