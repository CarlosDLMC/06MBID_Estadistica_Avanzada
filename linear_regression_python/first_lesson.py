import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return 0.5 * t ** 2 - t

fig, ax = plt.subplots()
x = np.linspace(-2, 4, 100)
y = [f1(t) for t in x]

ax.plot(x, y)
plt.show()

print(f1(1))