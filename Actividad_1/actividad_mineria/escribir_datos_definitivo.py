import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

apiUrl = "https://api.pro.coinbase.com"
sym = "BTC-USD"
# sym = "BNB-USD"
# sym = "LINK-USD"
# sym = "ETH-USD"
# sym = "LTC-USD"
# sym = "DOGE-USD"
# sym = "ADA-USD"
# sym = "DOT-USD"
# sym = "XMR-USD"
# sym = "SOL-USD"
# sym = "DOT-USD"

end_date = datetime.now().date().isoformat()
day = timedelta(days=1)
start_date = "2021-07-07"

def get_prices(sym, end_date, start_date):
    barsize = "86400"
    parameters = {
        "start": start_date,
        "end": end_date,
        "granularity": barsize,
    }
    headers = {"content-type": "application/json"}
    data = requests.get(f"{apiUrl}/products/{sym}/candles", params=parameters, headers=headers)
    datos = data.json()[::-1]
    return datos

precios = get_prices(sym, end_date=end_date, start_date=start_date)

fechas = pd.date_range(start=start_date, end=end_date).to_list()
fechas = [time.strftime("%Y-%m-%d") for time in fechas]

todo_junto = [f"{sym[:3]},{fechas[i]},{precios[i][2]},{precios[i][1]},{precios[i][3]},{precios[i][4]}\n" for i in range(len(precios))]

with open("historicos/modificados/Solana_modificado.csv", "a") as coin:
    coin.writelines(todo_junto)