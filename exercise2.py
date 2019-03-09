# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/cereal.csv')
# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Cereal Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        Info about cereal and its sugar and carb content.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=df['sugars'],
                    y=df['carbo'],
                    mode='markers',
                    text=df['name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 10,
                        'opacity': 0.8  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                )
            ],
            'layout': {
                'title': 'Cereal Data',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Sugars (g)'},
                'yaxis': {'title': 'Carbs (g)'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)