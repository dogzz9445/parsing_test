import requests
import json

def market_names_checker(func):
    def wrapper(markets):
        if len(markets) > 1:
            ','.join(markets)
        elif len(markets) == 0:
            return
        query_string = {"markets":markets}
        func(query_string)
    return wrapper

url_orderbook = "https://api.upbit.com/v1/orderbook"
url_ticker = "https://api.upbit.com/v1/ticker"

@market_names_checker
def get_orderbook(markets):
    response = requests.request("GET", url_orderbook, params=markets)
    if response.status_code == 200:
        json_response = json.loads('[{""status\':200, \'data\':response.text}]')
        return json_response
    return 

get_orderbook('KRW-BTC')