# Python Libraries
import os
import sys
import base64
import datetime
import io
import pandas as pd
import random


# Dash components
import dash
from dash.dependencies import Input, Output
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
checklist_list = None

colors = None
vendor_positions = None
vendor_colors = None

state = ''

# LOAD DATA for scores
def load_data(weight1, weight2, weight3, weight4):
    global weights, vendor_dictionary, sorted_vendors, sorted_scores, sorted_score_data, colors, vendor_positions, vendor_colors, checklist_list
    weights = [weight1, weight2, weight3, weight4]
    vendor_dictionary = import_data(filename, weights)
    sorted_vendors, sorted_scores = get_all_scores(vendor_dictionary)
    sorted_vendors = list(sorted_vendors)
    sorted_score_data = {'Vendor' : sorted_vendors, 'Score': sorted_scores}
    checklist_list = []
    for i in sorted_vendors:
        checklist_list.append(dict({'label': str(i), 'value' : str(i)}))

    checklist_list.sort(key=lambda x: x['label'], reverse=False)

    colors = []
    if state == 'highlight':
        for i in range(len(sorted_vendors)):
            colors.append('#8686FF')

        if vendor_positions == None:
            vendor_positions = get_new_vendor_positions(sorted_vendors)
        else:
            new_vendor_positions = get_new_vendor_positions(sorted_vendors)
            for vendor in vendor_positions:
                if new_vendor_positions[vendor] > vendor_positions[vendor]:
                    colors[new_vendor_positions[vendor]] = '#86FF86'
                elif new_vendor_positions[vendor] < vendor_positions[vendor]:
                    colors[new_vendor_positions[vendor]] = '#FF8686'
            vendor_positions = new_vendor_positions
    else:
        if vendor_colors == None:
            vendor_colors = {}
            for vendor in sorted_vendors:
                vendor_colors[vendor] = color_hash(vendor)
        for i in range(len(sorted_vendors)):
            colors.append(vendor_colors[sorted_vendors[i]])

# PARSE UPLOAD FILE
def parse_contents(contents, file_name):
    global filename
    filename = file_name[:len(file_name)-5]
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        if 'csv' in file_name:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(contents)
        elif 'xlsx' in file_name:
            # Assume that the user uploaded an excel file
            read_file = pd.read_excel(io.BytesIO(decoded))
            read_file.to_csv('data/' + filename + '.csv', index = None, header = False, float_format = '%.2f%%')
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

#Update the data input based on the upload file
def upload_data(list_of_contents, file_name):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, file_name)]
        return children

# LOAD GRAPH
def load_score_graph(weight1, weight2, weight3, weight4):
    # Load data from file
    load_data(weight1, weight2, weight3, weight4)

    scores = list(sorted_scores)
    vendors = list(sorted_vendors)

    fig = go.Figure([
        go.Bar(
            x=scores,
            y=vendors,
            texttemplate='%{y}: %{x:,.3%}',
            textposition='auto',
            marker_color=list(colors),
            orientation='h',
        )
    ])

    fig.update_xaxes(range=[0, 1])
    fig.update_layout(
        title={
            'text': "Vendor Scores",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=10, r=10, t=50, b=10),
        xaxis_tickformat='%',
        yaxis=dict(
            showticklabels=False
        )
    )

    return fig


# Load graph with stats to compare
def load_stats_graph(vendors=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                     stat = 'Total Failure Rate'):
    stat_data = []
    if stat == 'Total Failure Rate':
        for i in vendors:
            stat_data.append(vendor_dictionary[i].get_total_failure_rate())
    elif stat == 'Average Days Past PO':
        for i in vendors:
            stat_data.append(vendor_dictionary[i].get_avg_days_past_PO())
    elif stat == 'Average Cost Away from Target':
        for i in vendors:
            stat_data.append(vendor_dictionary[i].get_avg_cost_away_from_target())
    elif stat == 'Average Lot Size':
        for i in vendors:
            stat_data.append(vendor_dictionary[i].get_avg_lot_size())

    stat_fig = go.Figure([
        go.Bar(
            x=vendors,
            y=stat_data,
            text=stat_data,
            textposition='auto',
            marker_color=list(colors),
        )
    ])

    if stat == 'Total Failure Rate' or stat == 'Average Cost Away from Target':
        stat_fig.update_layout(
            title={
                'text': stat,
                'x': 0.5
            },
            yaxis={
                'title': '',
                'tickformat': ',.0%'
            },
            margin={
                'l': 10,
                'r': 20,
                'b': 10,
                't': 40
            }
        )
        stat_fig.update_traces(texttemplate='%{text:,.1%}')
    else:
        stat_fig.update_layout(
            title={
                'text': stat,
                'x': 0.5
            },
            margin={
                'l': 10,
                'r': 20,
                'b': 10,
                't': 40
            }
        )
        stat_fig.update_traces(texttemplate='%{text:,.2f}')
    return stat_fig


# GENERATE TABLE
def generate_table():
    fig = go.Figure(data=[go.Table(header=dict(values=['Vendor', 'Scores']),
                 cells=dict(values=[list(sorted_score_data['Vendor']), sorted_scores]))
                     ])
    fig.update_layout(title = "Sorted Vendor Scores (Lowest to Highest)")
    fig.layout.margin = dict(l=10, r=10, t=60, b=10)
    return fig


# GENERATE LOT SIZE PIE CHART
def load_num_orders_graph():
    num_orders = get_num_orders(vendor_dictionary, sorted_vendors)

    fig = go.Figure(go.Pie(
        labels=sorted_vendors,
        values=num_orders,
        hovertemplate = "%{label}: <br># Orders: %{value} </br> %{percent} <extra></extra>"
    ))

    fig.update_traces(
        textinfo='label',
        textfont_size=12,
        marker=dict(colors=colors)
    )

    fig.update_layout(
        title={
            'text': "Order Distribution from Vendors",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=0, r=0, t=50, b=20)
    )

    return fig

#Check to see if there is a requested file change using global file_name
def file_change(str = []):
    global filename
    if(str == None):
        return False
    val = str[0]
    val = val[:len(val)-5]
    if val == filename:
        return False
    return True


# APP CODE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Setup server variable
server = app.server

# APP LAYOUT
app.layout = html.Div(
        children=[
        html.H3(
            children='Vendor Dashboard',
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

    dcc.Tabs([
        dcc.Tab(label='Main Page', id='tab-1', children=[
            html.Div(
                children=[
                    html.Div(
                        className='row',
                        children=[
                            dcc.Graph(
                                id='sorted-scores',
                                className='box',
                                figure=load_score_graph(1,1,1,1)
                            ),
                            html.Div(
                                id='slider-box',
                                className='box',
                                children=[
                                    html.Div(
                                        className='sliders',
                                        children=[
                                            'Weight Sliders:',
                                            html.Div(
                                                children='1 - Least Influence; 10 - Most Influence',
                                                style={
                                                    'textAlign': 'center',
                                                    'marginBottom': 10,
                                                    'marginTop': 10
                                                }
                                            ),
                                            'Days Past PO',
                                            dcc.Slider(
                                                id='my-slider1',
                                                min=1,
                                                max=10,
                                                step=0.5,
                                                value=1,
                                                marks={
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

                                            'Non-conforming Units',
                                            dcc.Slider(
                                                id='my-slider2',
                                                min=1,
                                                max=10,
                                                step=0.5,
                                                value=1,
                                                marks={
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

                                            'Downstream Failures',
                                            dcc.Slider(
                                                id='my-slider3',
                                                min=1,
                                                max=10,
                                                step=0.5,
                                                value=4,
                                                marks={
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

                                            'Cost Difference from Target',
                                            dcc.Slider(
                                                id='my-slider4',
                                                min=1,
                                                max=10,
                                                step=0.5,
                                                value=1,
                                                marks={
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
                                        ]
                                    )
                                ]
                            ),
                            html.Div([
                                dcc.Upload(
                                    id='upload-data',
                                    children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files')
                                    ]),
                                    # Allow multiple files to be uploaded
                                    multiple=True
                                ),
                                html.Div(id='output-data-upload'),
                            ])
                        ]
                    ),
                    html.Div(
                        className='row',
                        children=[
                            dcc.Graph(
                                className='data-table box',
                                id='sorted-score-table',
                                figure=generate_table()
                            ),
                            dcc.Graph(
                                className='data-table box',
                                id='num-orders-chart',
                                figure=load_num_orders_graph()
                            )
                        ]
                    )
                ]
            )
        ]),

        dcc.Tab(label='Vendor Comparisons', id='tab-2', children=[
            html.Div(
                children=[
                    html.Div(
                        className='row',
                        children=[
                            dcc.Checklist(
                                id='vendor-checklist',
                                className='box',
                                options=checklist_list,
                                value=sorted_vendors
                            ),
                            dcc.Graph(
                                id='stats-compare',
                                className='box',
                                figure=load_stats_graph()
                            ),
                            dcc.Dropdown(
                                id='stat-dropdown',
                                className='box',
                                options=[
                                    {'label': 'Total Failure Rate', 'value': 'Total Failure Rate'},
                                    {'label': 'Average Days Past PO', 'value': 'Average Days Past PO'},
                                    {'label': 'Average Cost Away from Target', 'value': 'Average Cost Away from Target'},
                                    {'label': 'Average Lot Size', 'value': 'Average Lot Size'}
                                ],
                                value='Total Failure Rate'
                            )
                        ]
                    )
                ]
            ),
        ]),

    ])
])


#Update Graph Values
@app.callback(
    [Output('output-data-upload', 'children'),
     Output('sorted-scores', 'figure'),
     Output('sorted-score-table', 'figure'),
     Output('num-orders-chart', 'figure'),
     Output('vendor-checklist', 'options'),
     Output('vendor-checklist', 'value'),],
    [Input('my-slider1', 'value'),
     Input('my-slider2', 'value'),
     Input('my-slider3', 'value'),
     Input('my-slider4', 'value'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename')])
def update_output(value1, value2, value3, value4, list_of_contents, file_name):
    global vendor_colors, checklist_list, sorted_vendors
    #No new file upload
    if (not file_change(str = file_name)):
        return None, load_score_graph(value1, value2, value3, value4), generate_table(), load_num_orders_graph(), checklist_list, sorted_vendors
    else:
        #reset the vendor colors when a new file is uploaded
        vendor_colors = None;
        return upload_data(list_of_contents, file_name), load_score_graph(value1, value2, value3, value4), generate_table(), load_num_orders_graph(), checklist_list, sorted_vendors

@app.callback(
    Output('stats-compare', 'figure'),
    [Input('vendor-checklist', 'value'),
     Input('stat-dropdown', 'value')])
def update_stats_graph(vendors, stat_choice):
    return load_stats_graph(vendors=sorted(vendors), stat = stat_choice)

if __name__ == '__main__':
    app.run_server(debug=True)
