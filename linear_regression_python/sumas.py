import numpy as np
from time import time

N = 100000000
lista1 = list(range(N))
lista2 = list(range(N))

a = np.array(lista1.copy())
b = np.array(lista2.copy())

t1 = time()
total1 = np.dot(a, b)
t2 = time()

total2 = 0
for i in range(N):
    total2 += lista1[i] * lista2[i]

t3 = time()

print(total1, total2)
print("Tiempo en hacer el cálculo con numpy:", t2 - t1)
print("Tiempo en hacer el cálculo de forma clásica:", t3 - t2)
