import numpy as np
import matplotlib.pyplot as plt


# Input is any np.array (np.array([-105, 29, 110, -30, -5, 1]))
def sanityCheck(a):
    if np.shape(a) == 0:
        raise Exception("Fehler")


# x: any np.arange (np.arange(-10, 10, 0.1))
# coefficients: any np.array (np.array([-105, 29, 110, -30, -5, 1]))
def poly(x_poly, coefficients):
    f = 0
    for idx, coefficient in enumerate(coefficients):
        f += coefficient * x_poly ** idx
    return f


def derive(x_derive, coefficients):
    df = 0
    for idx, coefficient in enumerate(coefficients):
        df += idx * coefficient * pow(x_derive, idx - 1)
    return df


def integrate(x_integrate, coefficients):
    F = 0
    for idx, coefficient in enumerate(coefficients):
        F += (coefficient * pow(x_integrate, idx + 1)) / (idx + 1)
    return F


a = np.array([-105, 29, 110, -30, -5, 1])  # coefficients
sanityCheck(a)
x = np.arange(-10, 10, 0.1)
p = poly(x, a)
dp = derive(x, a)
pint = integrate(x, a)
plt.plot(x, p)
plt.plot(x, dp)
plt.plot(x, pint)

plt.xlim(-10, 10)
plt.ylim(-1000, 1000)
plt.title('Plynom, Ableitung sowie Stammfunktion A2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Polynom', 'Ableitung', 'Stammfunktion'])

plt.grid()
plt.show()
