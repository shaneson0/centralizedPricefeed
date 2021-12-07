

from conflux import (
    Account,
    Conflux,
    HTTPProvider,   
)
provider = HTTPProvider('https://test.confluxrpc.com')
c = Conflux(provider)

random_account = Account.create("shanxuan")
private_key_account = Account.from_key("0B6A7A4CF9C143421D948E6E33C7C84BF6882E39F8B2EE56FD29303E659E4F3B")

print(random_account.address)  # this is an hex address, you can use Address convert it to an base32 address
print(random_account.key)

transaction = {
    'from': 'cfxtest:aak2rra2njvd77ezwjvx04kkds9fzagfe6d5r8e957',
    'to': 'cfxtest:aak7fsws4u4yf38fk870218p1h3gxut3ku00u1k1da',
    'nonce': 1,
    'value': 1,
    # data: '0x',
    'gas': 100,
    'gasPrice': 1,
    'storageLimit': 100,
    'epochHeight': 100,
    'chainId': 1
}

signed_tx = Account.sign_transaction(transaction, random_account.key)
print(signed_tx.hash.hex())
print(signed_tx.rawTransaction.hex())

c.cfx.sendRawTransaction(signed_tx.rawTransaction.hex())

