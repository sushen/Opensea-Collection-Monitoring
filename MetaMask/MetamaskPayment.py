from acc_info import AccountInformation
from web3 import Web3


print(AccountInformation().from_account)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/21ed3d3934ee4b10887a8f4808174c99"))

connection = web3.isConnected()
print(connection)

from_account = AccountInformation.from_account
to_account = AccountInformation.to_account

private_key = AccountInformation.private_key

balance_f_a = web3.eth.get_balance(from_account)
balance_t_a = web3.eth.get_balance(to_account)

eth_balance_from_account = balance_f_a * .000000000000000001
eth_balance_to_account = balance_t_a * .000000000000000001

print(eth_balance_from_account)
print(eth_balance_to_account)

from_address = web3.toChecksumAddress(from_account)
to_address = web3.toChecksumAddress(to_account)

nonce = web3.eth.getTransactionCount(from_address)

tx = {
    "nonce": nonce,
    "to": to_address,
    "value": web3.toWei(0.001, "ether"),
    "gas": 21000,
    "gasPrice": web3.toWei(40, "gwei")
}

signe_tx = web3.eth.account.signTransaction(tx, private_key)

print(input("For Complete Transaction Press Enter:"))

tx_transaction = web3.eth.sendRawTransaction(signe_tx.rawTransaction)

print("Transaction Complete")



