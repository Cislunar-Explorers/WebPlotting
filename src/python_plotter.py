import time
import plotly.graph_objects as go
import numpy as np 
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

#Uncomment plotter and move to the Dash app section to run through webplotter

#Example plotter with pre-determined values 
# data = [1,3,2,4,3,3,2,3]

# fig = go.FigureWidget()
# fig.add_scatter()
# fig
# for i in range(len(data)):
#     time.sleep(0.3)
#     with fig.batch_update():
#         fig.data[0].y = data[:i]

# fig.show()


#Example plotter with values randomly generated over time using Numpy
# figure = go.FigureWidget()
# figure.layout.title = 'Example Scatter'
# n = 100
# x = np.linspace(0, 30, n)
# y = np.random.rand(n)
# figure.add_scatter(x=x, y=y)

# frame = 20
# first_scatter_plot = figure.data[0]

# for i in range(frame):
#   figure.show()
#   first_scatter_plot.y = np.random.rand(n) 
#   figure.update_layout(title=f'frame: {i + 1}');


#Example webplotter using Dash 
from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Example: Webplotter Using Dash With Selectable Y Axis'),
    html.P("Select Y-Axis Scaling:"),
    dcc.RadioItems(
        id='radio',
        options=['Scaling 1', 'Scaling 2'],
        value='Scaling 2'
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("radio", "value"))
def display_(radio_value):

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=[1, 2, 3], y=[40, 50, 60], # replace with your own data source
        name="yaxis data"), secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
        secondary_y=radio_value == 'Scaling 2',
    )

    # Add figure title
    fig.update_layout(title_text="Double Y Axis Example")

    # Set x-axis title
    fig.update_xaxes(title_text="Time (s)")

    # Set y-axes titles
    fig.update_yaxes(
        title_text="<b>Scaling 1 </b>Position", 
        secondary_y=False)
    fig.update_yaxes(
        title_text="<b>Scaling 2 </b>Position", 
        secondary_y=True)

    return fig


app.run_server(debug=True)

