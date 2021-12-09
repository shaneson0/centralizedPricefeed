


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
from util import *  
import time
from config import TRIANGLE_CONTRACT_ADDRESS, owner_private_key, owner_user_address


class ContractService():

    def __init__(self) -> None:
        self.provider = HTTPProvider('https://test.confluxrpc.com')
        self.c = Conflux(self.provider)

    def getContractAddress(self):
        self.contract_address = TRIANGLE_CONTRACT_ADDRESS
        return self.contract_address
            
    def getPrivateKey(self):
        private_key = owner_private_key
        return private_key

    def getOwnerAddress(self):
        owenrAdderss = owner_user_address
        return owenrAdderss

    def getContractABI(self):
        with open(current_path + '/../../build/TriangleOracle.abi') as json_file:
            triangleOracle_abi = json_file.read()

            return triangleOracle_abi
        
    def errorAndRetry(self):
        pass

    def gasEstimated(self, parameters):
        r = self.c.cfx.estimateGasAndCollateral(parameters, "latest_state")
        return r

    def register(self, _assertId):

        try:
            contract_address = self.getContractAddress()
            owner_address = self.getOwnerAddress()
            triangleOracle_abi = self.getContractABI()
            private_key = self.getPrivateKey()

            self.c.call_contract_method(contract_address, triangleOracle_abi, "register", _assertId)
            return True
        except:
            return False

        
    def getPrice(self, _assertID):
        contract_address = self.getContractAddress()
        contract_abi = self.getContractABI()
        Result, currentPrice = self._getPrice(contract_address, contract_abi, _assertID)
        return Result, currentPrice

    def putPrice(self, arguments):

        contract_address = self.getContractAddress()
        owner_address = self.getOwnerAddress()
        contract_abi = self.getContractABI()
        private_key = self.getPrivateKey()


        print("arguments:", arguments)

        result, txHash = self._putPrice(contract_address, owner_address, contract_abi, private_key, arguments)
        return result, txHash

    def _putPrice(self, contract_address, owner_address,  contract_abi, private_key, arguments):
        try:
            # initiate an contract instance with abi, bytecode, or address
            contract = self.c.contract(contract_address, contract_abi)
            data = contract.encodeABI(fn_name="putPrice", args=arguments)
            
            # get Nonce

            currentConfluxStatus = self.c.cfx.getStatus()   
            CurrentNonce =  self.c.cfx.getNextNonce(owner_address)

            parameters = {
                'from': owner_address,
                'to': contract_address,
                'data': data,
                'nonce': CurrentNonce,
                'gasPrice': 0x5
            }

            result = self.gasEstimated(parameters)
            
            parameters["storageLimit"] = result["storageCollateralized"] + 0x20
            parameters["gas"] = result["gasUsed"] + 0x100
            parameters["chainId"] = 1
            parameters["epochHeight"] = currentConfluxStatus["epochNumber"]

            # populate tx with other parameters for example: chainId, epochHeight, storageLimit
            # then sign it with account
            signed_tx = Account.sign_transaction(parameters, private_key)
            txHash = signed_tx.hash.hex()
            self.c.cfx.sendRawTransaction(signed_tx.rawTransaction.hex())
            return True, txHash

        except:
            traceback.print_exc()
            return False, ""

    def _getPrice(self, contract_address, triangleOracle_abi, _assertID):
        try:
            currentPrice = self.c.call_contract_method(contract_address, triangleOracle_abi, "valueFor", _assertID)
            return True, currentPrice

        except:
            traceback.print_exc()
            return 

if __name__ == "__main__":

    from eth_utils import to_bytes

    symbol = "CFX"
    assertId = "0x65784185a07d3add5e7a99a6ddd4477e3c8caad717bac3ba3c3361d99a978c29"

    timestamp = int(time.time())
    price = 207733055000000032

    
    contractServiceInstance = ContractService()

    #   function putPrice(bytes32 _id, int256 price, uint256 timestamp) public onlyOwner {
    arguments = [assertId, price, timestamp]
    Result, TxHash = contractServiceInstance.putPrice(arguments)
    print(Result, TxHash)

    # Get Price
    Result, currentPrice = contractServiceInstance.getPrice(assertId)
    print(Result, currentPrice)

# True 0x17ce68fb96d0e8fd1ba243b6003e022f1e3a944a8818182ee280883c5336c086
# True (207733055000000032, 1638858468, 200)
    