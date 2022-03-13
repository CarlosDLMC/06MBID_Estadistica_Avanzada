import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

non_decimal = re.compile(r'[^\d]+')

for line in open('csvs/moore.csv'):
    r = line.split('\t')
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

fig, ax = plt.subplots(ncols=2, nrows=1)
ax[0].scatter(X, Y)
ax[0].set(title='Exponencial', xlabel='Años', ylabel='Transistores')
# X = np.log(X)
Y = np.log(Y)
ax[1].scatter(X, Y)
ax[1].set(title='Logarítmico', xlabel='Años', ylabel='log(Transistores)')
denominator = np.dot(X, X) - X.mean() * X.sum() # El usa otra formula
a = (np.dot(X, Y) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * np.dot(X, X) - X.mean() * np.dot(Y, X)) / denominator
Yhat = a * X + b
ax[1].plot(X, Yhat)
plt.show()

print("a =", a, ",b =", b)
print(10 ** a)

d1 = Y - Yhat
d2 = Y - Y.mean()
ssr = np.dot(d1, d1)
sst = np.dot(d2, d2)

r2 = 1 - ssr / sst
print("R2 = ", r2)

# log(tc) = a * year + b
# tc = 10 ** (a * year) * 10 ** b
# 2 * tc = 2 * 10 ** (a * year) * 10 ** b = 10 ** log(2) * 10 ** (a * year) * 10 ** b
# 10 ** (a * year2) * 10 ** b = 10 ** log(2) * 10 ** (a * year1) * 10 ** b
# 10 ** (a * year2) = 10 ** log(2) * 10 ** (a * year1)
# 10 ** (a * year2) = 10 ** (a * year1 + log(2))
# a * year2 = a * year1 + log(2)
# year2 - year1 = dy = log(2) / a

print("Tiempo para duplicarse:", np.log(2)/a, "años")
