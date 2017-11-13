import gzip
import simplejson
import csv
import time
import plotly
plotly.tools.set_credentials_file(username='TusharMurarka', api_key='uMzgn8HNc9ah29sW64k0')

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import operator as op


import numpy as np
import pandas as pd


df = pd.read_csv('out.csv')
sample_data_table = FF.create_table(df.head())
#py.plot(sample_data_table, filename='sample-data-table')

trace1 = go.Scatter(
                    x=df['reviewerID'], y=['overall'], # Data
                    mode='lines', name='try' # Additional options
                   )

layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1], layout=layout)

py.plot(fig, filename='simple-plot-from-csv')
