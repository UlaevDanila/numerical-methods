import numpy as np
import matplotlib.pyplot as plt
import os

def main_calc(a, b, epsilon, y0):
    x = np.arange(a, b+epsilon, epsilon) 
    y = np.zeros(len(x))
    y[0] = y0

    def f(x,y):
         return (y**2 + (x**2)*y)/(x**3)

    for i in range(len(x)-1):                                                                       
        k1 = f(x[i],y[i])
        k2 = f((x[i]+epsilon/2),(y[i] + epsilon*k1/2))
        k3 = f((x[i]+epsilon/2),(y[i] + epsilon*k2/2))
        k4 = f((x[i] + epsilon),(y[i] + epsilon*k3))
        y[i+1] = y[i] + epsilon/6*(k1 + 2*k2 + 2*k3 + k4) 

    c1 = x[0]/y[0] - 1/x[0]
    y1 = x**2/(c1*x + 1)

    fig,ax = plt.subplots()
    plt.axis("equal")
    ax.plot(x,y, label = 'Метод Рунге-Кутта', marker = "o")
    ax.plot(x,y1, label = 'Аналитическое решение')
    plt.legend()
    plt.show()

    fid,ax = plt.subplots()
    plt.axis("equal")
    ax.plot(x,y, label = 'Метод Рунге-Кутта' )
    plt.legend()
    plt.show()

    fid,ax = plt.subplots()
    plt.axis("equal")
    ax.plot(x,y1, label = 'Аналитическое решение' )
    plt.legend()
    plt.show()

    return(x, y, y1)