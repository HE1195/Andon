from dash import Dash, html, dcc, Input, Output
import plotly.express as px


def build_board():
    pass


def build_rolling_msg():
    pass


app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    id="banner",
                    className="banner",
                    children=[
                        html.Div(
                            id="banner-text",
                            children=[
                                html.H5("SIEMENS"),
                                html.H6("Schaltanlagenwerk Frankfurt  - Andon Board Kostenstelle 605"),
                            ],
                        ),
                        html.Div(
                            id="banner-logo",
                            children=[
                            ],
                        ),
                    ],
                ),
                html.Div(
                    id="tabs",
                    className="tabs",
                    children=[
                        dcc.Tabs(
                            id="app-tabs",
                            value="tab2",
                            className="custom-tabs",
                            children=[
                                dcc.Tab(
                                    id="Control-chart-tab",
                                    label="Control Charts Dashboard",
                                    value="tab2",
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                            ],
                        )
                    ],
                )
            ],
        )
    ]
)

# @app.callback(
#
# )
# def update

if __name__ == '__main__':
    app.run_server(debug=True)


