from decimal import Decimal
from requests import Session
import requests
import cryptocompare
import time
import json

Prices = []
USDprice = ""

def tryethprice():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'ethereum', 'convert': 'USD' }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '15f8bbf5-3527-4234-952e-28a0e3d5362f'
    } 
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    info = json.loads(response.text)
    info = json.loads(response.text)['data']['1027']['quote']['USD']['price']
    return info

def getvalue(wallet):
    global USDprice

    url = f"https://deep-index.moralis.io/api/v2/{wallet}/balance?chain=eth"
    USDprice = cryptocompare.get_price('ETH', currency='USD').get("ETH")["USD"]

    headers = {
        "accept": "application/json",
        "X-API-Key": "yFsFQPj6zULbj9SNBoQLSWdgvX9nU0aIrW0XDnZHVg4EtxgsvMwvLkjUzz52zrwJ"
    }

    return requests.get(url, headers=headers).text

def getwalletprices(wallets:list):
    for i in wallets:
        Prices.append(Decimal(float(json.loads(getvalue(i))["balance"])) / Decimal(10) ** 18)

def PricesToUSD():
    global value
    value = 0   

    for i in Prices:    
        value += float(i) * float(tryethprice())
    Prices.clear()

    return value

while True:
    getwalletprices(["0x515ced994d4aab97db79dcb6c62751ed1f19f42f"])
    USD = PricesToUSD()
    print(USD)
    time.sleep(30)
