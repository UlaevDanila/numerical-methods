import numpy as np

def f(x):
    return (x**2)*np.cos(1000*x)
N = 2
s = 1

while abs(s) > 0.0000001:
    s = 0
    s1 = 0
    s2 = 0
    x = np.linspace(0, 1, N)

    for i in range(N-1):
        s1 =s1 + (x[i+1]-x[i])/8*(f(x[i]) + 3*f((2*x[i]+x[i+1])/3)+3*f((x[i]+2*x[i+1])/3)+f(x[i+1]))

    N = N*2
    x = np.linspace(0, 1, N)

    for i in range(N-1):
        s2 = s2 + (x[i+1]-x[i])/8*(f(x[i]) + 3*f((2*x[i]+x[i+1])/3)+3*f((x[i]+2*x[i+1])/3)+f(x[i+1]))

    s = s2 - s1

print(s2)
