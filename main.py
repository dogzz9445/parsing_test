import numpy as np
import pandas as pd
import upbit 
from time import sleep

if __name__ == '__main__':

    market_names = upbit.getMarketNames()
    if market_names is False:
        print('Failed to load market names')
        return

    while True:
        orderbook = upbit.getOrderBook('KRW-BTC')
        if orderbook is not False:
            for unit in orderbook[0]['orderbook_units']:
                print(unit)