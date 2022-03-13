import pandas as pd
from datetime import datetime

lista = pd.date_range(start="2018-09-09",end="2020-02-02").to_list()
lista = [time.strftime("%Y-%m-%d") for time in lista]

print(lista)
