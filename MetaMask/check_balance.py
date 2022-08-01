"""
 --**************************************************--
|| This apps give you the value of ether of a wallet ||
 --**************************************************--

We use two api to make this apps
web3 api come from https://infura.io/
Api Key Comes From https://www.cryptocompare.com/cryptopian/api-keys

"""
import cryptocompare

from web3 import Web3


# print(AccountInformation().from_account)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/21ed3d3934ee4b10887a8f4808174c99"))

connection = web3.isConnected()
# print(connection)


account = "0x01F30E80638F0c10533b78818475E54a9F66799B"


balance_f_a = web3.eth.get_balance(account)
eth_balance_from_account = balance_f_a * .000000000000000001

eth_current_price = cryptocompare.get_price('ETH', currency='USD')

# print(eth_current_price)

eth_price = eth_current_price['ETH']['USD']


print(f"Ethereum: {eth_balance_from_account}")
print(f"Usd: {eth_balance_from_account * eth_price}")
