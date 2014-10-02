#!/usr/bin/env python

import numpy as np
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import Data, Heatmap, Stream, Layout, Figure

N = 50
map = np.array([[-((i - N/2.0)**2 + (j - N/2.0)**2) for j in xrange(N)]
                    for i in xrange(N)])
x = np.array([(i - N/2.0) for i in xrange(N)])
y = x
z = np.exp(map/(N/2.0))

heatmap = Heatmap(z=z, x=x, y=y)
data = Data([heatmap])
layout = Layout(title='2D normal distribution')

figure = Figure(data=data, layout=layout)

unique_url = py.plot(figure, filename='heatmap_test', auto_open=False)
print 'URL: {0}'.format(unique_url)
