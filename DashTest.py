import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


from ConvertJsonToCsv import date_as_string

app = Dash(__name__)

df = pd.read_csv(f"dinos_meta_data_{date_as_string}.csv")

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['Woche'].min(),
        df['Woche'].max(),
        step=None,
        value=df['Woche'].min(),
        marks={str(week): str(week) for week in df['Woche'].unique()},
        id='date-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('date-slider', 'value'))
def update_figure(selected_week):
    filtered_df = df[df['Woche'] == selected_week]

    fig = px.line(filtered_df, x="Woche", y="Anzahl Kandidaten")

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
