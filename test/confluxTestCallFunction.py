

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

# // Result
# {
#   "jsonrpc": "2.0",
#   "result": {
#     "gasLimit": "0x6d60",
#     "gasUsed": "0x5208",
#     "storageCollateralized": "0x80"
#   },
#   "id": 1
# }

def gasEstimated(parameters):
    r = c.cfx.estimateGasAndCollateral(parameters, "latest_state")
    return r


def convertToBytes(a_string):
    encoded_string = a_string.encode()
    byte_array = bytearray(encoded_string)
    return byte_array

def test_contract_call(contract, triangleOracle_abi_str):
    try:
        # c.call_contract_method(contract, triangleOracle_abi_str, "putPrice", price, source, symbol, price_dimension)
        currentPrice = c.call_contract_method(contract, triangleOracle_abi_str, "getPrice")
        print("currentPrice: ", currentPrice)

    except:
        traceback.print_exc()
#    {
#       chainId: 1029,
#       networkId: 1029,
#       epochNumber: 1117476,
#       blockNumber: 2230973,
#       pendingTxNumber: 4531,
#       bestHash: '0x8d581f13fa0548f2751450a7dabd871777875c9ccdf0d8bd629e07a7a5a7917a'
#    }
# arguments = [price, source, symbol, price_dimension]

def gasEstimated(parameters):
    r = c.cfx.estimateGasAndCollateral(parameters, "latest_state")
    return r

def send_contract_call(contract_address, user_testnet_address,  contract_abi, private_key, arguments):
    try:
        # initiate an contract instance with abi, bytecode, or address
        contract = c.contract(contract_address, contract_abi)
        data = contract.encodeABI(fn_name="putPrice", args=arguments)
        
        # get Nonce

        currentConfluxStatus = c.cfx.getStatus()   
        CurrentNonce =  c.cfx.getNextNonce(user_testnet_address)

        parameters = {
            'from': user_testnet_address,
            'to': contract_address,
            'data': data,
            'nonce': CurrentNonce,
            'gasPrice': 0x5
        }

        result = gasEstimated(parameters)
        
        parameters["storageLimit"] = result["storageCollateralized"] + 0x20
        parameters["gas"] = result["gasUsed"] + 0x100
        parameters["chainId"] = 1
        parameters["epochHeight"] = currentConfluxStatus["epochNumber"]

        # populate tx with other parameters for example: chainId, epochHeight, storageLimit
        # then sign it with account
        signed_tx = Account.sign_transaction(parameters, private_key)

        print(signed_tx.hash.hex())
        print(signed_tx.rawTransaction.hex())
        c.cfx.sendRawTransaction(signed_tx.rawTransaction.hex())

    except:
        traceback.print_exc()

provider = HTTPProvider('https://test.confluxrpc.com')
c = Conflux(provider)

private_key = "0B6A7A4CF9C143421D948E6E33C7C84BF6882E39F8B2EE56FD29303E659E4F3B"
user_testnet_address = "cfxtest:aate5nxwmdrdavgwjb46ntn3k6zfym9z76s1jckvud"
shanxuan_Account = Account.from_key(private_key)

Account.create()


with open(current_path + '/../build/triangleOracle.abi') as json_file:

    triangleOracle_abi = json_file.read()
    contract_address = "cfxtest:acdseeaw57ktgz85sfy3g0ntgnr1vf59v2aznxpd1c"
    test_contract_call(contract_address, triangleOracle_abi)


