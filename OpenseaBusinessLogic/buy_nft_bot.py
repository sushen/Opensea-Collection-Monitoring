# TODO : Go to Base Website - https://opensea.io/
import time
from Bots.bot_ActivityPage import BotActivityPage
from Bots.bot_BuyPage import BotBuyPage

# xpath variables
nft_eth_price_xpath = "//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--amount']"
nft_names_xpath = "//div[@role='listitem']//child::div[@class='AssetCell--container']"
floor_prices_xpath = "//a[@class='chakra-link css-166ifkv']"
nft_click_xpath = "//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq styles__CoverLink-sc-nz4knd-1 givILt']"
ACTIVITY_URL = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
               "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
               "eventTypes][0]=AUCTION_CREATED "


buy_page = BotBuyPage()


buy_page.driver.get("https://opensea.io/")
print(input("Please connect your metamask then hit enter >>>>> "))

for i in range(1000):
    buy_page.driver.get(ACTIVITY_URL)
    buy_page.driver.implicitly_wait(10)
    print(input("Wating to load nft, this will be excluded later >>>> "))

    nft_names = buy_page.driver.find_elements_by_xpath(nft_names_xpath)
    nft_name = nft_names[-1].text

    nft_eth_prices = buy_page.driver.find_elements_by_xpath(nft_eth_price_xpath)
    nft_eth_price = nft_eth_prices[-1].text

    nft_floor_prices = buy_page.driver.find_elements_by_xpath(floor_prices_xpath)
    nft_floor_price = nft_floor_prices[-1].text

    print(f"NFT name : {nft_name} \n"
          f"NFT price in eth : {nft_eth_price} \n"
          f"NFT floor price : {nft_floor_price} \n")

    if float(nft_floor_price) > float(nft_eth_price):
        nft_click = buy_page.driver.find_elements_by_xpath(nft_click_xpath)
        nft_click[-1].click()
        buy_page.test_buy_button()

# TODO : Start The repeat loop and Continue...
