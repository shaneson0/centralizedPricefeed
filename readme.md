<!--
 * @Author: your name
 * @Date: 2021-10-26 22:13:04
 * @LastEditTime: 2021-10-26 22:34:20
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /triangleBlockchainOracle/readme.md
-->

# Centralized-pricefeed

Centralized-pricefeed is a Centralized blockchain oracle service, reading data from binance and okex api, and writing data to the contract.


## Perpare

``` bash


npm install -g conflux-truffle

# recommend using venv in python
pip install python-binance
pip install cryptography
pip install conflux
pip install pymysql
pip install dbutils


# for email sdk

pip install --upgrade sentry-sdk

```

## ABI Generation

We need to generate an ABI from the triangleOracle.sol. 

``` bash
git clone https://github.com/Conflux-Chain/conflux-abigen.git

go install ./cmd/cfxabigen

brew update
brew tap ethereum/ethereum
brew install solidity

sudo solc --abi contracts/triangleOracle.sol -o build

```
## Compile and deploy contracts 

``` bash
cfxtruffle compile

cfxtruffle migrated --network testnet

```
### Mysql prepare

``` bash

# Doing in DB-Client (such as Mysql Workbench ...)

create db name triangleOracle

import db from src/db/oracle_price.sql

```

### Run service


``` bash
# recommend using venv in python

cd src

python task/readLatestPrice.py --symbol CFX

```

### Usage Example

``` python

from conflux import (
    Account,
    Conflux,
    HTTPProvider,
)
import json
from cfx_address import Address
import os
current_path = os.path.dirname(os.path.abspath(__file__))
import traceback

provider = HTTPProvider('https://test.confluxrpc.com')
c = Conflux(provider)

def test_contract_call(contract, triangleOracle_abi_str):
    try:
        # c.call_contract_method(contract, triangleOracle_abi_str, "putPrice", price, source, symbol, price_dimension)
        currentPrice = c.call_contract_method(contract, triangleOracle_abi_str, "getPrice")
        print("currentPrice: ", currentPrice)

    except:
        traceback.print_exc()

with open(current_path + '/../build/triangleOracle.abi') as json_file:

    triangleOracle_abi = json_file.read()
    contract_address = "cfxtest:acdseeaw57ktgz85sfy3g0ntgnr1vf59v2aznxpd1c"

    test_contract_call(contract_address, triangleOracle_abi)
    # currentPrice:  334698400000000000

```











