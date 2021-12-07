


from conflux import (
    Account,
    Conflux,
    HTTPProvider,
)


provider = HTTPProvider('https://test.confluxrpc.com')
c = Conflux(provider)

def getContractABI():
    with open( '../build/priceFeed.abi') as json_file:
        priceFeed_abi = json_file.read()

        return priceFeed_abi


priceFeedAddress = "cfxtest:acbye06eytpawj66wu8csz4ffkw5cbu7eu6wrje220"
contract_abi = getContractABI()

priceFeedInstance = c.contract(priceFeedAddress, contract_abi)
lastGoodPrice = priceFeedInstance.fetchPrice()
print(lastGoodPrice)

# lastGoodPrice = priceFeedInstance.getPrice()
# print(lastGoodPrice)

