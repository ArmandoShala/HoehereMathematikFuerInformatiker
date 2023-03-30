import numpy as np

u = 2000.
m_0 = 10000.
q = 100.
g = 9.8

"""
Output h für Schrittweite summierte trapezregel 

"""

def Tf(f, a, b, n):
    xi = np.array([a + i * ((b - a) / n) for i in range(1, n)], dtype=np.float64)
    h = (b - a) / n
    return h * ((f(a) + f(b)) / 2 + np.sum(f(xi)))

a = 0
b = 30
h = 2
n = (a - b)/h

def v(t):
    return u * np.log(m_0/(m_0 - q * t)) - g * t

h_trap = Tf(v, a, b, 3)
print("Höhe h =", h_trap)

def ddv(t):
    return u * q**2/(m_0 - q * t)**2


tol = 1e-1
x = np.arange(a, b + tol, tol)

max_x_ddf = 0
for i in x:
    if np.abs(ddv(i)) > np.abs(ddv(max_x_ddf)):
        max_x_ddf = i

# Trapezregel:
print("h für Trapezregel: ")
print("h ≤ sqrt({} / (|ddv({})|*({}-{})) * 12)".format(tol,max_x_ddf,b,a))
print("h ≤", np.sqrt(tol/((b - a) * np.abs(ddv(max_x_ddf))) * 12))