'''
Author: your name
Date: 2021-10-21 13:46:39
LastEditTime: 2021-10-21 19:06:45
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/test/binance_websocket_test.py
'''


import asyncio
from binance import AsyncClient, BinanceSocketManager
from binance.enums import *


async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    
    # start any sockets here, i.e a trade socket
    ts = bm.trade_socket('CFXUSDT')
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print(res)

    await client.close_connection()



if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())





