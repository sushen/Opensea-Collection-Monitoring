import whatismyip


class IpAddress:
    @staticmethod
    def ip_address():
        online = whatismyip.amionline()
        print(online)

        if online:
            address = whatismyip.whatismyip()
            print(address)
            return address
        else:
            print("you dont have internet connection")


# IpAddress().ip_address()
