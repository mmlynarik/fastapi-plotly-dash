from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import pandas as pd


def create_dash_app(prefix: str = "/dash/") -> Dash:
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv'
    )

    app = Dash(__name__, routes_pathname_prefix=prefix)

    app.layout = html.Div(
        [html.H1('Stock Tickers'),
         dcc.Dropdown(
             id='my-dropdown',
             options=[
                 {'label': 'Tesla', 'value': 'TSLA'},
                 {'label': 'Apple', 'value': 'AAPL'},
                 {'label': 'Coke', 'value': 'COKE'}
             ],
             value='TSLA'
         ),
         dcc.Graph(id='my-graph')
         ], className="container"
    )

    @app.callback(Output('my-graph', 'figure'), Input('my-dropdown', 'value'))
    def update_graph(selected_dropdown_value):
        dff = df[df['Stock'] == selected_dropdown_value]
        return {
            'data': [{
                'x': dff.Date,
                'y': dff.Close,
                'line': {
                    'width': 3,
                    'shape': 'spline'
                }
            }],
            'layout': {'margin': {'l': 30, 'r': 20, 'b': 30, 't': 30}}
        }

    return app
