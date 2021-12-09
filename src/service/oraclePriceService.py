'''
Author: your name
Date: 2021-10-25 01:16:40
LastEditTime: 2021-11-02 15:42:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/src/service/oraclePriceDao.py
'''


from dao.oraclePriceDao import oraclePriceDao
from rpc import BinanceHolder, OkexHolder
from rpc.BinanceHolder import BinanceHolder
from rpc.OkexHolder import OkexHolder
from service.contractService import ContractService
import json

class OraclePriceService():
    
    def __init__(self):
        self.oracleDao = oraclePriceDao()
        self.binanceHolder = BinanceHolder()
        self.okexHolder = OkexHolder()
        self.confluxService = ContractService()


    # price = 329240000
    # source = '[{"price": 329240000, "avg_time": 5, "platform": "okex"}]'
    # symbol = convertToBytes('CFX')
    # price_dimension = 9
    # contract_address = "cfxtest:acaugnpsxzn614b0hh7dh61n8ydygv507yv4ku5nx5"
    # arguments = [price, source, symbol, price_dimension]
    def convertToBytes(self, a_string):
        encoded_string = a_string.encode()
        byte_array = bytearray(encoded_string)
        return byte_array



    def putRemotePrice(self, assertId, price, timestamp):
        arguments = [assertId, price, timestamp]
        res, txHash = self.confluxService.putPrice(arguments)
        return res, txHash
        

    def getRemotePrice(self, symbol):
        
        binance_res, binance_avg_price, binance_avg_time = self.binanceHolder.getAvgPrice(symbol)

        okex_res, okex_avg_price, okex_avg_time = self.okexHolder.getAvgPrice(symbol)

        print("binance_res: ", binance_res, ", okex_res : ", okex_res)

        res = False
        price = 0
        avg_time = 0
        source = []

        # binance resuls is error
        if binance_res is not True and okex_res is True:
            price = okex_avg_price
            res = okex_res
            avg_time = okex_avg_time
            source = [{
                "price": price,
                "avg_time": avg_time,
                "platform": "okex"
            }]

        # okex resuls is error
        if okex_res is not True and binance_res is True:
            price = binance_avg_price
            res = binance_res
            avg_time = binance_avg_time
            source = [{
                "price": price,
                "avg_time": avg_time,
                "platform": "binance"
            }]
        
        # normal sitation
        if binance_res is True and okex_res is True:
            price = int((binance_avg_price + okex_avg_price) / 2.0)
            res = True
            avg_time = binance_avg_time
            source = [{
                "price": binance_avg_price,
                "avg_time": binance_avg_time,
                "platform": "binance"
            },{
                "price": okex_avg_price,
                "avg_time": okex_avg_time,
                "platform": "okex"
            }]
        
        
        return res, price, avg_time, json.dumps(source)



    def insertRemotePrice(self, source, price, symbol, avg_time, txHash):
        res = self.oracleDao.insert( source, price, symbol, avg_time, txHash)
        return res


    # 分页查询
    def checkRemotePrice():
        pass


        
        



















































