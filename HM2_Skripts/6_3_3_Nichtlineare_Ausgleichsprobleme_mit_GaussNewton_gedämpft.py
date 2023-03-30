import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

"""
=======================================================================================================================
INPUT
=======================================================================================================================
"""

x = np.arange(0, 2.1, 0.2)  # Messwerte xi
y = np.array([39.55, 46.55, 50.13, 51.75, 55.25, 56.79, 56.78, 59.13, 57.76, 59.39, 60.08], dtype=np.float64)  # Messwerte yi

tol = 1e-5  # Fehlertoleranz
max_iter = 30  # Maximale Iterationen
pmax = 4  # Maximale Dämpfung

# Grenzen für den Intervall und "Schrittweite"
rangeA = 0
rangeB = 3
stepAccuracy = 0.001

# np Funktion aus der Aufgabenstellung
def U_np(t, lam):
    return lam[0] + (lam[1] - lam[0]) * (1 - np.exp(-t / lam[2]))

"""
=======================================================================================================================
"""

lam0 = np.array([3, -1], dtype=np.float64)  # Startvektor für Iteration

# Plot der Daten
plt.figure(1)
plt.plot(x, y, '*')
plt.xlabel('t')
plt.ylabel('U(t)')
plt.title("Plot Data as scatter plot")
plt.grid()
plt.show()

def f(x, a):
    return a[0] * sy.exp(a[1] * x)

a = sy.symbols('a:{n:d}'.format(n=lam0.size))
g = sy.Matrix([y[k] - f(x[k], a) for k in range(x.shape[0])])  # Fehlerfunktion für alle (xi, yi)
Dg = g.jacobian(a)

g_lambda = sy.lambdify([a], g, 'numpy')
Dg_lambda = sy.lambdify([a], Dg, 'numpy')

k = 0
lam = np.copy(lam0)
increment = tol + 1
err_func = np.linalg.norm(g_lambda(lam)) ** 2

while increment > tol and k <= max_iter:
    # QR-Zerlegung von Dg(lam)
    [Q, R] = np.linalg.qr(Dg_lambda(lam))
    delta = np.linalg.solve(R, -Q.T @ g_lambda(lam)).flatten()
    # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
    # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann

    # Dämpfung
    p = 0
    while p <= pmax and np.linalg.norm(g_lambda(lam + delta / (2 ** p))) ** 2 >= np.linalg.norm(g_lambda(lam)) ** 2:
        p += 1

    if p > pmax:
        p = 0

    # Update des Vektors Lambda
    lam = lam + delta / (2 ** p)

    err_func = np.linalg.norm(g_lambda(lam)) ** 2
    increment = np.linalg.norm(delta)
    print('Iteration: ', k)
    print('lambda = ', lam)
    print('Inkrement = ', increment)
    print('Fehlerfunktional =', err_func)
    print()
    k = k + 1

# fixme plot data with fit
# plt.figure(2)
# plt.plot(x, U_np(x, lam), 'r')
# plt.show()

exit()