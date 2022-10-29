from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H1('Position Vs. Time'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["X-Coordinate", "Y-Coordinate", "Z-Coordinate","Velocity","Acceleration"],
        value=["X-Coordinate"],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(positions):
    df = px.data.gapminder() # replace with your own data source
    mask = df.continent.isin(positions)
    fig = px.line(df[mask], 
        x="Time", y="Position", color='country')
    return fig


app.run_server(debug=True)