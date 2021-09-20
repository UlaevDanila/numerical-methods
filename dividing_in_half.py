import numpy as np

def f(x):
    return(np.cos(x)-x)

xmin = 0
xmax = 1

while xmax - xmin>0.001:
    xmid = (xmin + xmax)/2
    if f(xmin)*f(xmid)>0:
        xmin = xmid
    else:
        xmax = xmid

print(xmid)
