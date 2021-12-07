
#coding=utf8



DEBUG = False

import sys


if DEBUG is False:
    import sentry_sdk
    sentry_sdk.init(
        "https://6a0d73088d3f42eea1b9dcd46791d1c8@o1075757.ingest.sentry.io/6077933",
        
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )




# Adán SDPC, [Nov 21, 2021 at 12:53:01 AM]:
# Testnet addresses:
# BtcUsdPriceFeed: 0x8594B74645644b6a5fdE15597D3ADc15C77284A1
# CfxUsdtPriceFeed: 0x81cc73426944cC15BE22a3d7c812282E66F2c689
# EthUsdPriceFeed: 0x80DfFcbD9Fa48553fbC98aa7c21D50Ae47753C89

# Mainnet addresses:
# BtcUsdPriceFeed: 0x84E250b43337512B04aa5449e3A15FB715b78E88
# CfxUsdtPriceFeed: 0x86e9A67C92455afa725CC01b2036e47cd4dd9929
# EthUsdPriceFeed: 0x8Fd10Ad4913DC1F0049B46BfeD9F061e100B7ED9

import time
from rpc.BinanceHolder import BinanceHolder
from conflux import (
    Account,
    Conflux,
    HTTPProvider,
)


provider = HTTPProvider('https://main.confluxrpc.com')
c = Conflux(provider)

print(c.clientVersion)

test_address = 'cfx:acbsrshg7gaxfj683fv3v3ys6895yawf2j5sed44uy'

with open("../build/priceFeed.abi") as fp:
    contract_abi = fp.read()

pre_price = 0
pre_price_timestamp = 0

cur_price = 0

binanceholder = BinanceHolder()


def ServiceStart():
    msg = "【启动】sentry服务启动！"

    print(msg)

    if DEBUG is False:
        sentry_sdk.capture_message(msg)

def UpdatePrice():
    msg = "【价格更新】, 更新锚定价格为： %d"%(cur_price)
    
    print(msg)

    if DEBUG is False:
        sentry_sdk.capture_message(msg)


def BinanceAndWitnetPriceException(binancePrice, witnetPirce):
    msg = "Danger! 价格差异大于5, witnet: %d, binnace %d"%(witnetPirce, binancePrice)
    
    print(msg)

    if DEBUG is False:
        sentry_sdk.capture_message(msg)

while True:

    (price, _timestamp, status) = c.call_contract_method(test_address, contract_abi, 'valueFor', "0x65784185a07d3add5e7a99a6ddd4477e3c8caad717bac3ba3c3361d99a978c29")
    
    # {'id': 9132862, 'price': '0.28660000', 'qty': '40.00000000', 'quoteQty': '11.46400000', 'time': 1638150879142, 'isBuyerMaker': False, 'isBestMatch': True}
    # 假如网络异常，拿不到币安的价格就先不用管。
    try:
        _binancePriceResult = binanceholder.getRecentTrade()
        binancePrice = _binancePriceResult["price"]
    except:
        binancePrice = price

    print("price: %d, binancePrice: %d, pre_price_timestamp: %d, _timestamp: %d, status: %d"%(price, binancePrice, pre_price_timestamp, _timestamp, status))

    if status == 200:
        if pre_price == 0 and pre_price_timestamp == 0:
            pre_price_timestamp = _timestamp
            pre_price = price
            ServiceStart()
        
        cur_price = price

        # 假如时间超过1小时，则更新锚定价格
        if _timestamp != pre_price_timestamp:
            pre_price_timestamp = _timestamp
            pre_price = cur_price
            UpdatePrice()

        # 假如binancePrice和当前价格价格差5%，报警
        if abs(cur_price - binancePrice) > min(cur_price, binancePrice) * 0.05:
            BinanceAndWitnetPriceException(binancePrice, cur_price)

      
    # sleep 5 min
    sys.stdout.flush()
    time.sleep(5 * 60)




