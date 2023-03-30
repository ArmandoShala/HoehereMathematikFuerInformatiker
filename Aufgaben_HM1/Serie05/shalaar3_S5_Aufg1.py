import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.exp(pow(x, 2)) + pow(x, -3) - 10


def derive_function(functionToDerive, x):
    h = 1e-6
    return (functionToDerive(x + h) - functionToDerive(x - h)) / (2 * h)


def a1NewTon(startValue, times):
    loopVar = 0
    while loopVar <= times:
        print(loopVar, startValue)
        startValue = startValue - f1(startValue) / derive_function(f1, startValue)
        loopVar = loopVar + 1


def a1NewtonSimp(startValue, times):
    loopVar = 0
    firstValue = startValue
    while loopVar <= times:
        print(loopVar, startValue)
        startValue = startValue - f1(startValue) / derive_function(f1, firstValue)
        loopVar = loopVar + 1


def sekantenVerfahren(currValue, prevValue, times):
    loopVar = 0
    # Sekantenverfahren mit den Startwerten x0 = -1.0 und x1 = -1.2

    while loopVar <= times:
        nextValue = currValue - ((currValue - prevValue) / (f1(currValue) - f1(prevValue))) * f1(currValue)
        print(loopVar, nextValue)
        prevValue = currValue
        currValue = nextValue
        loopVar = loopVar + 1


# a1NewTon(2, 5)
print(derive_function(f1, 0.5))
# a1NewtonSimp(0.5, 5)
# sekantenVerfahren(-1.2, -1.0, 5)

plt.figure(1)
x_axis = np.arange(-3.5, 3.5, 0.1)
f = f1(x_axis)

plt.plot(x_axis, f)
plt.plot(x_axis, x_axis * 0, linestyle='-')  # solid line at y = 0

plt.xlim(-3.5, 3.5)
plt.ylim(-10, 10)

plt.xlabel('x')
plt.ylabel('y')

plt.legend([
    'e^(x^2) + x^-3 -10'
    , 'Abszisse'
])
plt.title('Serie 5, A1')

plt.grid()
plt.show()
