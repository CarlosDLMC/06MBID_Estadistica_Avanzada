import requests
import pandas as pd
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

pair = "adausd"

parameters = {
    "step": 86400,
    "limit": 1000
}

req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}/", params=parameters)
if "data" in req.text:
    req = req.json()["data"]["ohlc"]

    print(req)
    print(len(req))
else:
    print(req.text)