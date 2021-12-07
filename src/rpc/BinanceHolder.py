'''
Author: your name
Date: 2021-10-22 03:56:30
LastEditTime: 2021-11-02 15:47:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/src/rpc/BinanceHolder.py
'''

from binance import Client
import json
import traceback

api_key = "d75VjZ9Z5GEtZnkzKUNAvMOneVFI5RMXAGgRWbx6aZtdCF269zMa5Bg6fmUNXLAD"
api_secret = "qbfY2PLOQQxJyl2tPMTsLCKVGeloXuR3SgJHDWcOHhQPQNsVLZpjwnUIjfQD18AW"

    
# /api/v3/avgPrice
# Current average price for a symbol.

# /api/v3/ticker/price


class BinanceHolder():

    def __init__(self) -> None:
        self.client = Client(api_key, api_secret)
        self.price_dimansion = 10 ** 18

    def getAvgPrice(self, symbol):
        try:
            avg_price = self.client.get_avg_price(symbol='CFXUSDT')
            
            print("biancne getavg price: ", avg_price)

            binance_avg_time = int(avg_price['mins'])
            binance_avg_price = int( float(avg_price['price'])  *  self.price_dimansion )


            #  {'mins': 5, 'price': '0.32856984'}
            # binance_res, binance_avg_price, binance_avg_timse

            print("binance_avg_price, binance_avg_time : ", binance_avg_price, binance_avg_time)
            return True, binance_avg_price, binance_avg_time
        except:

            traceback.print_exc()
            return False, 0, 0

    def getRecentTrade(self, symbol="CFXUSDT"):
        trades = self.client.get_recent_trades(symbol='CFXUSDT')
        res = trades[-1]
        # 改成正常时间戳，2021-11-29 09:54:39
        res["time"] = res["time"] / 1000
        res["price"] = int(float(res["price"]) * (10**6))
        return res


    def errorAndRetry(self):
        pass

if __name__ == "__main__":
    symbol = "CFX"
    price_dimansion = 10 ** 18
    binanceHolder = BinanceHolder()
    Res, binance_avg_price, binance_avg_time = binanceHolder.getAvgPrice(symbol, price_dimansion)
    print(Res, binance_avg_price, binance_avg_time)
