'''
Author: your name
Date: 2021-10-21 03:44:39
LastEditTime: 2021-10-21 13:11:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/test/websocketTest.py
'''


import time

from binance import ThreadedWebsocketManager

api_key = "d75VjZ9Z5GEtZnkzKUNAvMOneVFI5RMXAGgRWbx6aZtdCF269zMa5Bg6fmUNXLAD"
api_secret = "qbfY2PLOQQxJyl2tPMTsLCKVGeloXuR3SgJHDWcOHhQPQNsVLZpjwnUIjfQD18AW"

def main():

    symbol = 'BNBBTC'

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)

    # multiple sockets can be started
    twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)

    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['bnbbtc@miniTicker', 'bnbbtc@bookTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()


if __name__ == "__main__":
   main()