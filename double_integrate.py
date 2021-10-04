import numpy as np

def f(x,y):
    return 1/(1+x**2+y**2)
N = 2
s = 1

while abs(s) > 0.0000001:
    s = 0
    s1 = 0
    s2 = 0
    x = np.linspace(0, 1, N)
    y = np.linspace(0, 1, N)
    for i in range(N-1):
        for j in range(N-1):
            s1 = s1 + (x[i+1]-x[i])*f((x[i]+x[i+1])/2,(y[j]+y[j+1])/2)*(y[j+1]-y[j])

    N = N*2
    x = np.linspace(0, 1, N)
    y = np.linspace(0, 1, N)

    for i in range(N-1):
        for j in range(N-1):
            s2 = s2 + (x[i+1]-x[i])*f((x[i]+x[i+1])/2,(y[j]+y[j+1])/2)*(y[j+1]-y[j])

    s = s2 - s1

print(np.log2(N))
print(s2)
