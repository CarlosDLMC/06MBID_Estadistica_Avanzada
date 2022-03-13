import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

X = []
dates = []
Y = []
i = 0

for line in open('actividad_mineria/historicos/modificados-28-febrero/bitcoin_modificado.csv'):
    r = line.split(',')
    try:
        y = float(r[4])
    except:
        continue
    Y.append(y)
    dates.append(datetime.strptime(r[1], "%Y-%m-%d"))
    X.append(i)
    i += 1

X = np.array(X)
Y = np.array(Y)
fig, ax = plt.subplots()
ax.scatter(dates, Y, s=1)
ax.set(title='Precio de Bitcoin por día', xlabel='Años', ylabel='Precio en dólares')
plt.show()
Y = np.log(Y)
fig, ax = plt.subplots()
ax.scatter(dates, Y, s=1)
ax.set(title='Logaritmo del precio de Bitcoin por día', xlabel='Años', ylabel='log(precio en dólares)')
denominator = np.dot(X, X) - X.mean() * X.sum() # El usa otra formula
a = (np.dot(X, Y) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * np.dot(X, X) - X.mean() * np.dot(Y, X)) / denominator
Yhat = a * X + b
ax.plot(dates, Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()
ssr = np.dot(d1, d1)
sst = np.dot(d2, d2)

r2 = 1 - ssr / sst
print('a =', a)
print('b =', b)
print("R2 = ", r2)
print("ssr = ", ssr)
print("sst = ", sst)
