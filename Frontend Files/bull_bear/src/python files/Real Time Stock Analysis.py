from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import dash
import pandas as pd
import numpy as np
import requests

from datetime import datetime

import yfinance as yf

app = Dash()
tickerdf=pd.read_csv('/Users/lordvoldemort/IdeaProjects/PythoN/NSE Tickers List.csv')
tickerlist=tickerdf['SYMBOL']

def create_dropdown(option, id_value):
    return html.Div(
        [
            html.H2("Select Ticker of the Stock",
                    style={"padding":"0px 100px 0px 100px"}),
            dcc.Dropdown(option, id=id_value, value=option[0])
        ]
    )

app.layout = html.Div([

    html.Div([
        create_dropdown(tickerlist,"Tickers-select"),
    ],style={'display':'flex', 'margin':'auto',"width":"800px", "justify-content":"space-around"}),
    # dcc.Dropdown(tickerlist,id="Tickers-select",value='RELIANCE'),

    dcc.Graph(id="candles"),
    dcc.Graph(id="indicator"),

    html.Div([
        dcc.RangeSlider(0,420,20,value=[0,420], id="range-slider"),
    ],id='range-slider-container',
        style={'width':'800px','margin':'auto','padding-top':'10px',"justify-content":"space-around"}
    ),

    dcc.Interval(id="interval", interval=30000),
])

@app.callback(
    Output("candles","figure"),
    Output("indicator","figure"),
    Input("interval","n_intervals"),
    Input("Tickers-select","value"),
    Input("range-slider","value"),

)

def update_figure(n_intervals, symbol,range_values):
    df = yf.download(tickers=symbol+'.NS', period='1d', interval='1m')
    print(df)

    df=df.iloc[range_values[0]:range_values[1]]

    candles = go.Figure(
        data=[
            go.Candlestick(
                x= df.index,
                open= df.Open,
                high= df.High,
                low= df.Low,
                close= df.Close,
            )
        ]
    )

    candles.update_layout(xaxis_rangeslider_visible=False,height=600)

    candles.update_layout(transition_duration=500)

    indicator = px.line(x=df.index,y=df.Close, height = 600)

    indicator.update_layout(transition_duration=500)

    return candles, indicator

if __name__ == '__main__':
    app.run_server(debug=False)