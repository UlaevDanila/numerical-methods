import numpy as np

def f(x):
    return np.cos(x) - x

def df(x): 
    return -np.sin(x) - 1

x = 1.0
n = 0

while abs(f(x)) > 0.0000001:
    x = x - f(x)/df(x)
    n+=1
    if n > 1000:
        break

print(n, x, f(x))