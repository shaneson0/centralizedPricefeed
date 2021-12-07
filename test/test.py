'''
Author: your name
Date: 2021-10-21 00:04:12
LastEditTime: 2021-10-21 03:44:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/test/test.py
'''

# $ export HTTP_PROXY="http://10.10.1.10:3128"
# $ export HTTPS_PROXY="http://10.10.1.10:1080"

from binance import Client

api_key = "d75VjZ9Z5GEtZnkzKUNAvMOneVFI5RMXAGgRWbx6aZtdCF269zMa5Bg6fmUNXLAD"
api_secret = "qbfY2PLOQQxJyl2tPMTsLCKVGeloXuR3SgJHDWcOHhQPQNsVLZpjwnUIjfQD18AW"

def main():
    client = Client(api_key, api_secret)

    # /api/v3/avgPrice
    # Current average price for a symbol.

    # /api/v3/ticker/price
    
    avg_price = client.get_avg_price(symbol='CFXUSDT')
    print(avg_price)

    aggregate_trades = client.get_aggregate_trades(symbol='CFXUSDT')
    print(aggregate_trades)



# status = client.get_system_status()

# {
#     "status": 0,        # 0: normal，1：system maintenance
#     "msg": "normal"     # normal or System maintenance.
# }



if __name__ == "__main__":
    main()


