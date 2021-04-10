
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

        
# async def getTradeTick(session, markets):
#     if len(markets) == 0:
#         return False
#     markets = {"market" : markets, "count" : 1}
#     response = requests.request("GET", TICKS, params=markets)
#     if response.status_code == 200:
#         json_response = json.loads(response.text)
#         return json_response
#     return False
