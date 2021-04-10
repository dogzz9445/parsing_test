import requests
import json
import asyncio
import aiohttp
import websockets

ORDERBOOK = "https://api.upbit.com/v1/orderbook"
TICKER = "https://api.upbit.com/v1/ticker"
TICKS = "https://api.upbit.com/v1/trades/ticks"
MARKETS = "https://api.upbit.com/v1/market/all"

def session_decorator(func):
    async def wrapper(markets: str, session = None):
        result = None
        if session == None:
            async with aiohttp.ClientSession() as session:
                return await func(session markets)
        return await func(session, markets)

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

async def getTradeTick(session, markets):
    async with session.get(TICKS, params=markets) as response:
        result = await response.text()
        print(result)
        return result
    return False

def getMarketNames():
    querystring = {"isDetails":"false"}
    response = requests.request("GET", MARKETS, params=querystring)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        return json_response
    return False

logger = logging.getLogger(__name__)

is_alive = True

import asyncio
import websockets

async def 

async def alive():
    while is_alive:
        logger.info('alive')
        await asyncio.sleep(300)


async def async_processing():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            try:
                message = await websocket.recv()
                print(message)

            except websockets.exceptions.ConnectionClosed:
                print('ConnectionClosed')
                is_alive = False
                break



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
