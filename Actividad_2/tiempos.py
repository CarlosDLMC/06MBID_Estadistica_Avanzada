
# Sacar ACF y PACF y las 3 graficas estas de tendencia ruido y estacionalidad
# trend, noise, seasonal
# Y analizar acada una diciendo porqué tal o cual cosa
# Y luego coger la predicción y pintarla como hizo ella en la clase y fuera
# Y si acaso decir porqué predice bien o mal o que
# y tampoco dio mucho mas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose

df_bitcoin = pd.read_csv('bitcoin.csv')

df_bitcoin['Date'] = pd.to_datetime(df_bitcoin.Date)
# df_bitcoin['variacion_diaria'] = df_bitcoin.apply(lambda row: row.Close - row.Open, axis=1)
df_bitcoin['variacion_diaria'] = df_bitcoin.apply(lambda row: (row.Close - row.Open) / row.Open * 100, axis=1)
# df_bitcoin['variacion_diaria'] = df_bitcoin.Close - df_bitcoin.Open
print(df_bitcoin)

high = df_bitcoin.High.to_numpy()

print(high, type(high), type(high[0]))
print(df_bitcoin["Date"][0])

plt.figure(figsize=(10,4))
plt.plot(df_bitcoin.variacion_diaria)
plt.title('Variación diaria del precio de bitcoin', fontsize=30)
plt.ylabel('Variación diaria (%)', fontsize=26)
plt.xlabel('Número de día', fontsize=26)
# for year in range(2013,2022):
#     plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)
plt.show()

# acf_plot = plot_acf(df_bitcoin.variacion_diaria, lags=50)
#
# plt.show()
#
# pacf_plot = plot_pacf(df_bitcoin.variacion_diaria, method='ywm')
# plt.show()

total_duration = 100
step = 0.01
time = np.arange(0, total_duration, step)
T = 15

print("variacion: ", list(df_bitcoin.Open))
series_periodic = np.sin((2*np.pi / T) * time)

lista = list(df_bitcoin.Open)
datos = [int(i) for i in lista]
results = seasonal_decompose(datos, model='additive', period=int(len(df_bitcoin.Open)/6))
trend_estimate = results.trend
periodic_estimate = results.seasonal
residual = results.resid

# plt.figure(figsize=(12, 10))
# plt.subplot(411)
# plt.plot(df_bitcoin.Open, label='Original time series', color='blue')
# plt.legend(loc='best')
# plt.show()
# plt.subplot(412)
# plt.plot(trend_estimate, label='Trend of time series', color='blue')
# plt.legend(loc='best')
# plt.show()
plt.subplot(413)
plt.plot(periodic_estimate, label='Seasonality of time series', color='blue')
plt.legend(loc='best')
plt.show()
plt.subplot(414)
plt.plot(residual, label='Decomposition residuals of time series', color='blue')
plt.legend(loc='best')
plt.show()