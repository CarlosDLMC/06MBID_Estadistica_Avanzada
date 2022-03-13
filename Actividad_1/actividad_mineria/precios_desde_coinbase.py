import requests
import pandas as pd
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

apiUrl = "https://api.pro.coinbase.com"
sym = "DOGE-USD"
end_date = datetime.now().date()
day = timedelta(days=1)

def get_prices(sym, end_date, days=200):
    barsize = "86400"
    timeStart = end_date - ((days - 1) * day)
    timeStart = timeStart.isoformat()
    end_date = end_date.isoformat()
    parameters = {
        "start": timeStart,
        "end": end_date,
        "granularity": barsize,
    }
    headers = {"content-type": "application/json"}
    data = requests.get(f"{apiUrl}/products/{sym}/candles", params=parameters, headers=headers)
    lista = data.json()
    print(lista)
    print(len(lista))
    precios = [x[3] for x in lista][::-1]
    print(len(precios))
    print(precios)
    return precios

# precios = get_prices(sym, end_date)
# fig, ax = plt.subplots(nrows=2)
# ax[0].plot(precios)

precios = get_prices(sym, end_date=datetime.strptime("7 07 2021", "%d %m %Y"))
fig, ax = plt.subplots()
ax.plot(precios)
plt.show()