import numpy as np
import pandas as pd
import upbit 
import math
import asyncio
import aiohttp
from time import sleep

async def async_get_trade_ticks(market_names):
    async with aiohttp.ClientSession() as session:
        for market in market_names:
            markets = {"market" : market['market'], "count" : 1}
            tradeticks = await upbit.getTradeTick(session, markets)
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