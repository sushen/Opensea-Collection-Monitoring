from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ActivityPage(BasePage):
    ACTIVITY_URL = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
                   "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
                   "eventTypes][0]=AUCTION_CREATED "
    ACTIVITY_TITLE = "Activity | OpenSea"

    NFT_NAMES = (By.XPATH, "//div[@role='listitem']//child::div[@class='AssetCell--container']")

    NFT_PRICES = (By.XPATH, "/div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--fiat-amount']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.ACTIVITY_URL)

    def get_first_nft_name(self, NFT_NAMES):
        self.get_element_text(NFT_NAMES)


    # def get_first_nft_price(self, driver):
    #     nft_prices = driver.find_elements_by_xpath(self.NFT_PRICE_XPATH)
    #     nft_price = nft_prices[-1].text
    #     return nft_price
