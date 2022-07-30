from acc_info import AccountInformation
from web3 import Web3


print(AccountInformation().from_account)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/21ed3d3934ee4b10887a8f4808174c99"))

connection = web3.isConnected()
print(connection)
