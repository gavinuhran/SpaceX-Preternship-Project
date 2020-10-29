# Python Libraries
import os
import sys


# Dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


# Imports functions and classes from include/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'include'))

from init_data import *
from dictionary_functions import *


# SET GLOBAL VARIABLES
filename = 'FakeData'

weights = None
vendor_dictionary = None
sorted_vendors = None
sorted_scores = None
sorted_score_data = None


# LOAD DATA
def load_data(weight3):
    global weights, vendor_dictionary, sorted_vendors, sorted_scores, sorted_score_data
    weights = [1, 1, weight3, 1]
    vendor_dictionary = import_data(filename, weights)
    sorted_vendors, sorted_scores = get_all_scores(vendor_dictionary)
    sorted_score_data = {'Vendor' : list(sorted_vendors), 'Score': sorted_scores}
    #sorted_score_data = dict(Vendor=list(sorted_vendors), Score=sorted_scores)


# LOAD GRAPH
def load_graph(weight3):
    # Load data from file
    load_data(weight3)

    # Create new figure
    sorted_score_fig = px.bar(sorted_score_data, x='Vendor', y='Score')
    sorted_score_fig.update_yaxes(range=[0, 100])
    return sorted_score_fig


# GENERATE TABLE
def generate_table():
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in list(sorted_score_data.keys())])
        ),
        html.Tbody([
            html.Tr([
                html.Td(vendor_dictionary[name].name),
                html.Td(sorted_scores[i])
            ])for i, name in enumerate(list(vendor_dictionary.keys()))
        ])
    ])


# APP CODE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# APP LAYOUT
app.layout = html.Div(

    [
    html.H3(
        children='SpaceX Dashboard',
        style={
            'textAlign': 'center'
        }
    ),

    html.Div(
        children='Vendor Analysis based on their previous performance',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(
        className='row',
        children=[
            dcc.Graph(
                id='sorted-scores',
                figure=load_graph(4)
            ),
        ]
    ),

    html.Div(
        className='slider1',
        style={
            'width': 500,
        },
        children=[
            dcc.Slider(
                id='my-slider',
                min=0,
                max=5,
                step=0.5,
                value=4,
                marks={
                    0: {'label': '0', 'style': {'color': '#f50'}},
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                },
                included=False,
            ),

            html.Div(id='slider-output-container')
        ]
    ),

    generate_table()
])

@app.callback(
    dash.dependencies.Output('sorted-scores', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return load_graph(value)

if __name__ == '__main__':
    app.run_server(debug=True)
