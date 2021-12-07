'''
Author: your name
Date: 2021-10-20 03:34:02
LastEditTime: 2021-11-02 15:41:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/src/rpc/okex.py
'''



import sys
import os
from traceback import print_exc
cwdPath = os.getcwd()
sys.path.insert(0, cwdPath + "/third/")


import okex.account_api as account
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import okex.index_api as index
import okex.option_api as option
import okex.system_api as system
import okex.information_api as information
import okex.oracle_api as oracle
import json
import datetime
import traceback

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

time = get_timestamp()

instrument_id = "CFX-USDT-SWAP"
api_key = "7f2b08e6-3c19-4a36-a375-91abdb614779"
secret_key = "83441EF0A8E1DE1DF3ECB1CD01AAE01B"
passphrase = "xuan13924540343"


class OkexHolder():

    def __init__(self) -> None:
        self.spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
        self.price_dimansion = 10 ** 18
    def getAvgPrice(self, symbol):
        
        try:    
            result = self.spotAPI.get_deal(instrument_id="CFX-USDT", limit=50)
            
            # 50条接近5分钟，是否5分钟个人觉得不太重要，只要是一段时间的积累交易平均值即可。
            AvgPrice = 0.0
            AvgPriceCount = 0
            for item in result:
                AvgPrice = AvgPrice + float(item["price"])
                AvgPriceCount = AvgPriceCount + 1
            
            AvgPrice = AvgPrice / AvgPriceCount

            # okex_res, okex_avg_price, okex_avg_time
            okex_avg_price = int( AvgPrice * self.price_dimansion )
            
            # 暂时先写5，这里准备地应该是：result[0] - result[49] 的时间差
            okex_avg_time = 5   

            print(okex_avg_price, okex_avg_time)
            return True, okex_avg_price, okex_avg_time
        except:
            traceback.print_exc()
            return False, 0, 0

    def errorAndRetry(self):
        pass

if __name__ == '__main__':
    
    symbol = "CFX"
    okdexHolder = OkexHolder()
    price = okdexHolder.getAvgPrice(symbol)
    
    print(price)


