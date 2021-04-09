import requests
import json
import asyncio
import aiohttp
from requests import async

ORDERBOOK = "https://api.upbit.com/v1/orderbook"
TICKER = "https://api.upbit.com/v1/ticker"
TICKS = "https://api.upbit.com/v1/trades/ticks"
MARKETS = "https://api.upbit.com/v1/market/all"

async def getOrderBook(session, markets):
    if len(markets) == 0:
        return False
    markets = ','.join(markets)
    markets = {"markets":markets}
    response = requests.request("GET", ORDERBOOK, params=markets)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        return json_response
    return False

# async def getTradeTick(session, markets):
#     if len(markets) == 0:
#         return False
#     markets = {"market" : markets, "count" : 1}
#     response = requests.request("GET", TICKS, params=markets)
#     if response.status_code == 200:
#         json_response = json.loads(response.text)
#         return json_response
#     return False

async def getTradeTick(session, markets):
    async with session.get(pokemon_url) as resp:
        pokemon = await resp.json()
        print(pokemon['name'])
    response = requests.request("GET", TICKS, params=markets)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        return json_response
    return False

def getMarketNames():
    querystring = {"isDetails":"false"}
    response = requests.request("GET", MARKETS, params=querystring)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        return json_response
    return False


# def markets_names_checker(func):
#     async def wrapper(markets):
#         return await func(markets)
#     return wrapper

# def market_names_checker(func):
#     async def wrapper(markets):
#         if len(markets) == 0:
#             return
#         markets = {"market":markets, "count":1}
#         return await func(markets)
#     return wrapper

# orderbook = upbit.getTradeTick('KRW-BTC')
# if orderbook is not False:
#     for unit in orderbook[0]['orderbook_units']:
#         print(unit)
