import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from plotly import graph_objects as go
import os

df1 = pd.read_csv("GamePS4.csv")
df2 = pd.read_csv("GameXOne.csv")
df3 = pd.read_csv("GameNS.csv")

GameAll_Bar = dash.Dash()

PS4 = go.Bar(
    x = df1.game,
    y = df1.TotalSales,
    name='PS4'
)

XOne = go.Bar(
    x = df2.game,
    y = df2.TotalSales,
    name='XOne'
)

NS = go.Bar(
    x = df3.game,
    y = df3.TotalSales,
    name='NS'
)

server = GameAll_Bar.server

GameAll_Bar.layout = html.Div([
    dcc.Graph(id='Game sales Chart',
              figure=go.Figure(data=[PS4, XOne, NS],
                               layout=go.Layout(title = 'Game Sales Chart', barmode='stack'))
              )
    ])
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    GameAll_Bar.run_server(host='0.0.0.0',debug=True,port=port)