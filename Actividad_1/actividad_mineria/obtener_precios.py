from requests import Request, Session
import json
from pprint import pprint

latest_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
historical_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listing/historical"


parameters = {
    'symbol': 'BTC',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9d6036cf-d54d-4740-8f6d-a40884ed73fc'
    # 'X-CMC_PRO_API_KEY': 'e3763607-e592-4ba9-b6d5-3769d4a54290'
}

session = Session()
session.headers.update(headers)

response = session.get(historical_url, params=parameters)
in_json = json.loads(response.text)

pprint(in_json)
print("lo que nos interesa: ")
pprint(in_json['data']['BTC']['quote']['USD']['pricef'])
