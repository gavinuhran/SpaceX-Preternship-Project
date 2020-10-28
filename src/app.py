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

# Load data from file
filename = 'FakeData'
weights = [1, 1, 4, 1]
vendor_dictionary = init_data.import_data(filename, weights)

sorted_vendors, sorted_scores = dictionary_functions.get_all_scores(vendor_dictionary)
sorted_score_data = dict(Vendor=sorted_vendors, Score=sorted_scores)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

sorted_score_fig = px.bar(sorted_score_data, x='Score', y='Vendor', orientation='h')
sorted_score_fig.update_xaxes(range=[0, 1])

app.layout = html.Div(
    className='page-container',
    children=[
        html.H3(children='SpaceX Dashboard'),
        
        html.Div(
            className='row',
            children=[
                dcc.Graph(
                    id='sorted-scores',
                    figure=sorted_score_fig
                ) 
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
