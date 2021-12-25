# TODO : Go to Base Website - https://opensea.io/
import time

from Bots.bot_ActivityPage import BotActivityPage

acclivity = BotActivityPage()
acclivity.driver.get("https://opensea.io/")
acclivity.test_home_title()

# TODO : Login Using Meta Mask and Stop Script

# print(input("Connect Wallet :"))

# TODO : Find NFT Name
acclivity.driver.implicitly_wait(4)
# time.sleep(4)
NFT_NAMES = "(//div[@class = 'AssetCell--container'])"
NFT_NAMES_Elam = acclivity.driver.find_elements_by_xpath(NFT_NAMES)
print(NFT_NAMES_Elam)
print(NFT_NAMES_Elam[0].text)

for i in NFT_NAMES_Elam:
    print(i.text)


# TODO : Find NFT Price

# TODO : Find NFT Floor Price

# TODO : Compare Floor Price to NFT present Price

# TODO : Repeat this process using loop

# TODO : GO for Single NFT Page

# TODO : Buy Single NFT

# TODO : Start The repeat loop and Continue...


