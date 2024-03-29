import numpy as np
import matplotlib.pyplot as plt

"""
=======================================================================================================================
INPUT
=======================================================================================================================
"""

x = np.array([4, 6, 8, 10], dtype=np.float64)  # Stützpunkte (Knoten) xi
y = np.array([6, 3, 9, 0], dtype=np.float64)  # Stützpunkte (Knoten) yi
x_int = 9  # Zu interpolierender Wert

"""
=======================================================================================================================
"""

n = x.shape[0] - 1  # Anzahl Spline-Polynome
dim = 3

print(f'{n} Spline-Polynome {dim}. Grades (je {dim + 1} Koeffizienten) => {n} * {dim + 1} = {(dim + 1) * n} Unbekannte => Es braucht {(dim + 1) * n} Gleichungen.')

# Allgemeine Spline 3. Grades und deren Ableitungen:
# Si(x) = ai + bi(x - xi) + ci(x - xi)^2 + di(x - xi)^3
# Si'(x) = bi + ci * 2(x - xi) + di * 3(x - xi)^2
# Si''(x) = ci * 2 + di * 6(x - xi)
# Si'''(x) = di * 6

# Not-a-knot kubische Spline-Interpolation mit 4 Stützstellen
# -----------------------------------------------------------
A = np.array([
   # a0 a1 a2 b0 b1 b2 c0 c1 c2 d0 d1 d2
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # S0(x0) = y0 <=> a0 + b0(x0 - x0) + c0(x0 - x0)^2 + d0(x0 - x0)^3 = y0 <=> a0 = y0 (Spline 0 muss durch (x0, y0) gehen)
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # S1(x1) = y1 <=> a1 + b1(x1 - x1) + c1(x1 - x1)^2 + d1(x1 - x1)^3 = y1 <=> a1 = y1 (Spline 1 muss durch (x1, y1) gehen)
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # S2(x2) = y2 <=> a2 + b2(x2 - x2) + c2(x2 - x2)^2 + d2(x2 - x2)^3 = y2 <=> a2 = y2 (Spline 2 muss durch (x2, y2) gehen)
    [1, 0, 0, x[1]-x[0], 0, 0, (x[1]-x[0])**2, 0, 0, (x[1]-x[0])**3, 0, 0],  # S0(x1) = S1(x1) <=> S0(x1) = y1 <=> a0 + b0(x1 - x0) + c0(x1 - x0)^2 + d0(x1 - x0)^3 = y1 (Spline 0 und 1 müssen sich im Punkt (x1, y1) treffen <=> Spline 0 muss durch (x1, y1) gehen)
    [0, 1, 0, 0, x[2]-x[1], 0, 0, (x[2]-x[1])**2, 0, 0, (x[2]-x[1])**3, 0],  # S1(x2) = S2(x2) <=> S2(x2) = y2 <=> a1 + b1(x2 - x1) + c1(x2 - x1)^2 + d1(x2 - x1)^3 = y2 (Spline 1 und 2 müssen sich im Punkt (x2, y2) treffen <=> Spline 1 muss durch (x2, y2) gehen)
    [0, 0, 1, 0, 0, x[3]-x[2], 0, 0, (x[3]-x[2])**2, 0, 0, (x[3]-x[2])**3],  # S2(x3) = y3 <=> a2 + b2(x3 - x2) + c2(x3 - x2)^2 + d2(x3 - x2)^3 = y3 (Spline 2 muss durch (x3, y3) gehen (letzter Stützpunkt))
    [0, 0, 0, 1, -1, 0, 2*(x[1]-x[0]), 0, 0, 3*(x[1]-x[0])**2, 0, 0],  # S0'(x1) = S1'(x1) <=> S0'(x1) - S1'(x1) = 0 <=> b0 - b1 + c0 * 2(x1 - x0) - c1 * 2(x1 - x1) + d0 * 3(x1 - x0)^2 - d1 * 3(x1 - x1)^2 = 0 <=> b0 - b1 + c0 * 2(x1 - x0) + d0 * 3(x1 - x0)^2 = 0 (Keine Knicke zwischen S0 und S1)
    [0, 0, 0, 0, 1, -1, 0, 2*(x[2]-x[1]), 0, 0, 3*(x[2]-x[1])**2, 0],  # S1'(x2) = S2'(x2) <=> S1'(x2) - S2'(x2) = 0 <=> b1 - b2 + c1 * 2(x2 - x1) - c2 * 2(x2 - x2) + d1 * 3(x2 - x1)^2 - d2 * 3(x2 - x2)^2 = 0 <=> b1 - b2 + c1 * 2(x2 - x1) + d1 * 3(x2 - x1)^2 = 0 (Keine Knicke zwischen S1 und S2)
    [0, 0, 0, 0, 0, 0, 2, -2, 0, 6*(x[1]-x[0]), 0, 0],  # S0''(x1) = S1''(x1) <=> S0''(x1) - S1''(x1) = 0 <=> c0 * 2 - c1 * 2 + d0 * 6(x1 - x0) - d0 * 6(x1 - x1) = 0 <=> c0 * 2 - c1 * 2 + d0 * 6(x1 - x0) = 0 (Gleiche Krümmung zwischen S0 und S1)
    [0, 0, 0, 0, 0, 0, 0, 2, -2, 0, 6*(x[2]-x[1]), 0],  # S1''(x2) = S2''(x2) <=> S1''(x2) - S2''(x2) = 0 <=> c1 * 2 - c2 * 2 + d1 * 6(x2 - x1) - d1 * 6(x2 - x2) = 0 <=> c1 * 2 - c2 * 2 + d1 * 6(x2 - x1) = 0 (Gleiche Krümmung zwischen S1 und S2)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, -6, 0],  # NOT-A-KNOT: S0'''(x1) = S1'''(x1) <=> S0'''(x1) - S1'''(x1) = 0 <=> d0 * 6 - d1 * 6 = 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, -6]  # NOT-A-KNOT: S1'''(x2) = S2'''(x2) <=> S1'''(x2) - S2'''(x2) = 0 <=> d1 * 6 - d2 * 6 = 0
], dtype=np.float64)

b = np.array([
    y[0],  # S0(x0) = y0
    y[1],  # S1(x1) = y1
    y[2],  # S2(x2) = y2
    y[1],  # S0(x1) = y1
    y[2],  # S2(x2) = y2
    y[3],  # S2(x3) = y3
    0,  # S0'(x1) - S1'(x1) = 0
    0,  # S1'(x2) - S2'(x2) = 0
    0,  # S0''(x1) - S1''(x1) = 0
    0,  # S1''(x2) - S2''(x2) = 0
    0,  # S0'''(x1) - S1'''(x1) = 0
    0,  # S1'''(x2) - S2'''(x2) = 0
], dtype=np.float64)

print('\nLöse LGS Ax = b mit')
print(f'A = \n{A}')
print(f'b = {b}')

print('LGS wird gelöst...\n')

abcd = np.linalg.solve(A, b)
a = abcd[0:3]
b = abcd[3:6]
c = abcd[6:9]
d = abcd[9:]

print(f'x = {abcd}')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')

print('\nDiese Werte jetzt einsetzen in Si(x) = ai + bi(x - xi) + ci(x - xi)^2 + di(x - xi)^3:')

for i in range(n):
    print(f'\tS{i}(x) = {a[i]} + {b[i]} * (x - {x[i]}) + {c[i]} * (x - {x[i]})^2 + {d[i]} * (x - {x[i]})^3')

print('\nBestimmen, welches Spline-Polynom verwendet werden muss (Vergleich mit den Stützstellen)')

i = np.max(np.where(x <= x_int))  # Finde die Stützstelle, deren x-Wert am grössten, aber gerade noch kleiner ist als x_int
print(f'Für x_int = {x_int} muss S{i} verwendet werden.')

y_int = a[i] + b[i] * (x_int - x[i]) + c[i] * (x_int - x[i]) ** 2 + d[i] * (x_int - x[i]) ** 3

print(f'S{i}({x_int}) = {y_int}')


# PLOTTING
xx = np.arange(x[0], x[-1], (x[-1] - x[0]) / 10000)  # Plot-X-Werte

# Bestimme für jeden x-Wert, welches Spline-Polynom gilt
xxi = [np.max(np.where(x <= xxk)) for xxk in xx]

# Bestimme die interpolierten Werte für jedes x
yy = [a[xxi[k]] + b[xxi[k]] * (xx[k] - x[xxi[k]]) + c[xxi[k]] * (xx[k] - x[xxi[k]]) ** 2 + d[xxi[k]] * (xx[k] - x[xxi[k]]) ** 3 for k in range(xx.shape[0])]

plt.figure(1)
plt.grid()
plt.plot(xx, yy, zorder=0, label='spline interpolation')
plt.scatter(x, y, marker='x', color='r', zorder=1, label='measured')
plt.scatter(x_int, y_int, marker='X', color='fuchsia', label='interpolated')
plt.legend()
plt.show()
