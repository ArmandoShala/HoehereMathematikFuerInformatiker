import timeit

import numpy as np


# y = fact_rec(n) berechnet die Fakultät von n als fact_rec(n) = n * fact_rec(n -1) mit fact_rec(0) = 1
# Fehler, falls n < 0 oder nicht ganzzahlig
def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)


def fact_for(n, start=1):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else:
        fact = 1
        for i in range(start, n + 1):
            fact *= i
        return fact


rec = fact_rec(4)
fr = fact_for(4)

print(rec, fr)

t1 = timeit.timeit("fact_rec(500)", "from shalaar3_S1_Aufg3 import fact_rec", number=100)
t2 = timeit.timeit("fact_for(500)", "from shalaar3_S1_Aufg3 import fact_for", number=100)
print(t1, t2)

# FAQ:
# F1: Welche der beiden Funktionen ist schneller und um was für einen Faktor? Weshalb?
# Q1: Die Rekursive, um den Faktor 7.75 bis 10: print(t1 / t2)

# F2: Gibt es in Python eine obere Grenze für die Fakultät von n
# Q2.1: Ja, gibt es. Mit diesen Beispielen ist dies ersichtlich
# Q2.2: als ganze Zahl (vom Typ 'integer')?
# Versuchen Sie hierzu, das Resultat für n ∈ [190, 200] als integer auszugeben
print(fact_for(200, 190))
# Q2.3: als reelle Zahl (vom Typ 'float')?
# Versuchen Sie hierzu, das Resultat für n ∈ [170, 171] als float auszugeben
print(fact_for(171., 170.))
