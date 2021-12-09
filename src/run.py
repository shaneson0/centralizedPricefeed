'''
Author: your name
Date: 2021-10-24 18:48:40
LastEditTime: 2021-11-02 15:46:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/src/task/readLatestPrice.py
'''

import sys
import os
import time
cwdPath = os.getcwd()

sys.path.insert(0, cwdPath)

from service.oraclePriceService import OraclePriceService
import argparse
parser = argparse.ArgumentParser()


parser.add_argument("--symbol", help="rToken request module") 
assertId = "0x65784185a07d3add5e7a99a6ddd4477e3c8caad717bac3ba3c3361d99a978c29"

def getOpts():
    args = parser.parse_args()
    if args.symbol:
        symbol = args.symbol
        return symbol
    else:
        return None

if __name__ == "__main__":
    symbol = getOpts()

    if symbol is None:
        exit(0)

    oraclepriceservice = OraclePriceService()

    while True :

        symbol = "CFX"
        res, price, avg_time, source = oraclepriceservice.getRemotePrice(symbol)
    
        if res is True:
            timestamp = int(time.time())
            putRemotePriceResult, txHash = oraclepriceservice.putRemotePrice(assertId, price, timestamp)
            
            print("txHash : ", txHash)

            if putRemotePriceResult is True:
                result = oraclepriceservice.insertRemotePrice(source, price, symbol, avg_time, txHash)
            
            else:
                print("putRemotePrice error !")

        else:
            print("getRemotePrice is false")

        time.sleep(60 * 5)














