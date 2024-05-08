import numpy as np
import colorlover as cl
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots

# Q1 (a)
def samplegen(a):
    Z1 = np.random.normal(0,1,10000)
    Z2 = np.random.normal(0,1,10000)
    X1 = 5 + Z1
    X2 = 8 + 2*a*Z1 + 2*np.sqrt(1 - a*a)*Z2
    return X1, X2

xvalues = []

def showsample(a):
    x1, x2 = samplegen(a)
    xvalues.append([np.array(x1), np.array(x2)])
    print("a: ", a)
    print("x1: ", x1)
    print("x2: ", x2)

showsample(-0.5)
showsample(0)
showsample(0.5)
showsample(1)


#(b) and (c)
col = [[float(i)/float(len(cl.scales['5']['seq']['Blues'])-1), cl.scales['5']['seq']['Blues'][i]] for i in range(len(cl.scales['5']['seq']['Blues']))]

def contour():
    fig = make_subplots(rows=4, cols=1, subplot_titles=(f"2D contour with a = -0.5", f"2D contour with a = 0", f"2D contour with a = 0.5", f"2D contour with a = 1"))
    
    fig.add_trace(go.Histogram2dContour(x=xvalues[0][0], y=xvalues[0][1], colorscale=col, colorbar=dict(len=0.1, y= 0.95)), row=1, col=1)
    fig.add_trace(go.Histogram2dContour(x=xvalues[1][0], y=xvalues[1][1], colorscale=col, colorbar=dict(len=0.1, y= 0.65)), row=2, col=1)
    fig.add_trace(go.Histogram2dContour(x=xvalues[2][0], y=xvalues[2][1], colorscale=col, colorbar=dict(len=0.1, y= 0.35)), row=3, col=1)
    fig.add_trace(go.Histogram2dContour(x=xvalues[3][0], y=xvalues[3][1], colorscale=col, colorbar=dict(len=0.1, y= 0.1)), row=4, col=1)

    fig.update_layout(height=2600, width=1100)
    fig.show()


def histogram():
    fig = make_subplots(rows=4, cols=1, subplot_titles=(f"2D histogram with a = -0.5", f"2D histogram with a = 0", f"2D histogram with a = 0.5", f"2D histogram with a = 1"))
    
    fig.add_trace(go.Histogram2d(x=xvalues[0][0], y=xvalues[0][1], colorscale=col, colorbar=dict(len=0.1, y= 0.95)), row=1, col=1)
    fig.add_trace(go.Histogram2d(x=xvalues[1][0], y=xvalues[1][1], colorscale=col, colorbar=dict(len=0.1, y= 0.65)), row=2, col=1)
    fig.add_trace(go.Histogram2d(x=xvalues[2][0], y=xvalues[2][1], colorscale=col, colorbar=dict(len=0.1, y= 0.35)), row=3, col=1)
    fig.add_trace(go.Histogram2d(x=xvalues[3][0], y=xvalues[3][1], colorscale=col, colorbar=dict(len=0.1, y= 0.1)), row=4, col=1)

    fig.update_layout(height=2600, width=1100)
    fig.show()

histogram()
contour()