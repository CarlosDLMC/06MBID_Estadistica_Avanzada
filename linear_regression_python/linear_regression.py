import numpy as np
import matplotlib.pyplot as plt

# first we load the data
X = list()
Y = list()
for line in open('csvs/data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

# Ahora aplicamos las ecuaciones para calcular a y b. Usaremos las fórmulas de este tío del vídeo 6

denominator = np.dot(X, X) - X.mean() * X.sum() # El usa otra formula
a = (np.dot(X, Y) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * np.dot(X, X) - X.mean() * np.dot(Y, X)) / denominator

# calculated predicted Y
Yhat = a * X + b

plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()
ssr = np.dot(d1, d1)
sst = np.dot(d2, d2)

r2 = 1 - ssr / sst
print(r2)