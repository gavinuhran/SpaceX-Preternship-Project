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

import init_data
import dictionary_functions

# APP CODE
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def load_graph(value):
    # Load data from file
    filename = 'FakeData'
    weights = [1, 1, value, 1]
    vendor_dictionary = init_data.import_data(filename, weights)

    sorted_vendors, sorted_scores = dictionary_functions.get_all_scores(vendor_dictionary)
    sorted_score_data = dict(Vendor=list(sorted_vendors), Score=sorted_scores)

    sorted_score_fig = px.bar(sorted_score_data, x='Score', y='Vendor', orientation='h')
    sorted_score_fig.update_xaxes(range=[0, 1])
    return sorted_score_fig

'''
sorted_score_fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
'''


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
                id='sorted-scores'
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
                value=1,
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
])

@app.callback(
    dash.dependencies.Output('sorted-scores', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return load_graph(value)

if __name__ == '__main__':
    app.run_server(debug=True)
