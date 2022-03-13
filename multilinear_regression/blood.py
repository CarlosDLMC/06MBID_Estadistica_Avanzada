# The data (X1, X2, X3) are for each patient.
# X1 = systolic blood pressure
# X2 = age in years
# X3 = weight in pounds

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('csvs/mlr02.xls')
X = df.to_numpy()

plt.scatter(X[:, 1], X[:, 0])
plt.show()

plt.scatter(X[:, 2], X[:, 0])
plt.show()

df['ones'] = 1
Y = df['X1']
X = df[['X2', 'X3', 'ones']]
X2only = df[['X2', 'ones']]
X3only = df[['X3', 'ones']]

def get_r2(X, Y):
    w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
    Yhat = np.dot(X, w)
    d1 = Y - Yhat
    d2 = Y - Y.mean()
    return 1 - d1.dot(d1) / d2.dot(d2)

print(f'r2 for x2: {get_r2(X2only, Y)}')
print(f'r2 for x3: {get_r2(X3only, Y)}')
print(f'r2 for both: {get_r2(X, Y)}')