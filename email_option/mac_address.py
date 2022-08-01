import psutil

nics = psutil.net_if_addrs()

mac_address = nics['Ethernet'][0].address

print(mac_address)


