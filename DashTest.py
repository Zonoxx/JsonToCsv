import pandas as pd
import plotly.express as px

import dash
from dash import Dash, dcc, html

from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("dinos_meta_data.csv")


df = df.groupby(['Woche', 'Anzahl Kandidaten'])
df.reset_index(inplace=True)

app = Dash(__name__)

app.layout = html.Div([

    html.H1("DINOS Meta Data Table", style={'text-align': 'center'}),

    # dcc.Dropdown(id="slct_week",
    #              options=[
    #                  {"label": "Woche 1", "value": 1},
    #                  {"label": "Woche 2", "value": 2},
    #                  {"label": "Woche 3", "value": 3},
    #                  {"label": "Woche 4", "value": 4},
    #                  {"label": "Woche 5", "value": 5},
    #                  {"label": "Woche 6", "value": 6},
    #                  {"label": "Woche 7", "value": 7},
    #                  {"label": "Woche 8", "value": 8},
    #                  {"label": "Woche 9", "value": 9},
    #                  {"label": "Woche 10", "value": 10}],
    #              multi=False,
    #              value=1,
    #              style={'width': "40%"}
    #              ),

    dcc.Graph(id='dinos_meta_data', figure={})
])


@app.callback(
    [Output(component_id='dinos_meta_data', component_property='figure')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # dff = df.copy()
    # dff = dff[dff["Woche"] == option_slctd]

    # Plotly Express
    fig = px.bar(df, x="", y="Anzahl Kandidaten")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
