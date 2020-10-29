# Python Libraries
import os
import sys


# Dash components
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
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
def load_data(weight1, weight2, weight3, weight4):
    global weights, vendor_dictionary, sorted_vendors, sorted_scores, sorted_score_data
    weights = [weight1, weight2, weight3, weight4]
    vendor_dictionary = import_data(filename, weights)
    sorted_vendors, sorted_scores = get_all_scores(vendor_dictionary)
    sorted_score_data = {'Vendor' : list(sorted_vendors), 'Score': sorted_scores}
    #sorted_score_data = dict(Vendor=list(sorted_vendors), Score=sorted_scores)


# LOAD GRAPH
def load_graph(weight1, weight2, weight3, weight4):
    # Load data from file
    load_data(weight1, weight2, weight3, weight4)

    # Create new figure
    sorted_score_fig = px.bar(sorted_score_data, x='Vendor', y='Score')
    sorted_score_fig.update_yaxes(range=[0, 100])
    return sorted_score_fig


# GENERATE TABLE
def generate_table():
    fig = go.Figure(data=[go.Table(header=dict(values=['Vendor', 'Scores']),
                 cells=dict(values=[list(sorted_score_data['Vendor']), sorted_scores]))
                     ])
    return fig


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
                figure=load_graph(1,1,1,1)
            ),
        ]
    ),

    html.Div(
        children='Variable weight for Days Past PO',
        style={
            'textAlign': 'left',
        }
    ),

    html.Div(
        className='slider1',
        style={
            'width': 500,
        },
        children=[
            dcc.Slider(
                id='my-slider1',
                min=1,
                max=10,
                step=0.5,
                value=4,
                marks={
                    0: {'label': '0', 'style': {'color': '#f50'}},
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: '6',
                    7: '7',
                    8: '8',
                    9: '9',
                    10: '10',
                },
                included=False,
            ),

            html.Div(id='slider-output-container')
        ]
    ),
    html.Div(
        children='Variable weight for Non-Conforming Units',
        style={
            'textAlign': 'left',
        }
    ),
    html.Div(
        className='slider2',
        style={
            'width': 500,
        },
        children=[
            dcc.Slider(
                id='my-slider2',
                min=1,
                max=10,
                step=0.5,
                value=4,
                marks={
                    0: {'label': '0', 'style': {'color': '#f50'}},
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: '6',
                    7: '7',
                    8: '8',
                    9: '9',
                    10: '10',
                },
                included=False,
            ),

            html.Div(id='slider-output-container2')
        ]
    ),
    html.Div(
        children='Variable weight for Unit Failure Downstream',
        style={
            'textAlign': 'left',
        }
    ),
    html.Div(
        className='slider3',
        style={
            'width': 500,
        },
        children=[
            dcc.Slider(
                id='my-slider3',
                min=1,
                max=10,
                step=0.5,
                value=4,
                marks={
                    0: {'label': '0', 'style': {'color': '#f50'}},
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: '6',
                    7: '7',
                    8: '8',
                    9: '9',
                    10: '10',
                },
                included=False,
            ),

            html.Div(id='slider-output-container3')
        ]
    ),
    html.Div(
        children='Variable weight for cost away from target',
        style={
            'textAlign': 'left',
        }
    ),
    html.Div(
        className='slider4',
        style={
            'width': 500,
        },
        children=[
            dcc.Slider(
                id='my-slider4',
                min=1,
                max=10,
                step=0.5,
                value=4,
                marks={
                    0: {'label': '0', 'style': {'color': '#f50'}},
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: '6',
                    7: '7',
                    8: '8',
                    9: '9',
                    10: '10',
                },
                included=False,
            ),

            html.Div(id='slider-output-container4')
        ]
    ),

    html.Div(
        className='data-table',
        children=[
            dcc.Graph(
                id='sorted-score-table',
                figure= generate_table()
            ),
        ]
    ),
])

#Update Graph Values
@app.callback(
    [dash.dependencies.Output('sorted-scores', 'figure'),
    dash.dependencies.Output('sorted-score-table', 'figure')],
    [dash.dependencies.Input('my-slider1', 'value'),
    dash.dependencies.Input('my-slider2', 'value'),
    dash.dependencies.Input('my-slider3', 'value'),
    dash.dependencies.Input('my-slider4', 'value')])
def update_output(value1, value2, value3, value4,):
    return load_graph(value1, value2, value3, value4), generate_table()


if __name__ == '__main__':
    app.run_server(debug=True)
