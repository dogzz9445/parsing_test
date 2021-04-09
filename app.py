import numpy as np
import pandas as pd
import upbit 
import math
import asyncio
import aiohttp
from time import sleep

async def async_get_trade_ticks(market_names):
    if len(markets) == 0:
        return False
    markets = {"market" : markets, "count" : 1}
    async with aiohttp.ClientSession() as session:
        for market in market_names:
            if tradeticks != False:
                print(tradeticks)

if __name__ == '__main__':
    json_market_names = np.array(upbit.getMarketNames())
    if json_market_names is False:
        print('Failed to load market names')
    else:
        krw_market_names = []
        for market in json_market_names:
            if 'KRW' in market['market']:
                krw_market_names.append(market)

        # parsing state
        loop = asyncio.get_event_loop() 
        loop.run_until_complete(async_get_trade_ticks(krw_market_names))
        loop.close()
        # for market in krw_market_names:
        #     tradeticks = upbit.getTradeTick(market['market'])
        #     if tradeticks != False:
        #         print(tradeticks)

        # markets_names = np.array([])
        # for market in json_market_names:
        #     if 'KRW' in market['market']:
        #         korean_market_names.append(market)
        # if len(korean_market_names) != 0:
        #     markets_names = np.array_split(np.array(korean_market_names), math.ceil(len(korean_market_names) / 5))
            
        # while True:
        #     # parsing state
        #     for markets in markets_names:
        #         markets = list(map(lambda market : market['market'],markets))
        #         tradeticks = upbit.getTradeTick(markets)
        #         if tradeticks is not False:
        #             print('hello')
        #             print(tradeticks)
        #             # for unit in tradeticks[0]['orderbook_units']:
        #             #     print(unit)
        #         sleep(0.5)
        #         break
        #     break