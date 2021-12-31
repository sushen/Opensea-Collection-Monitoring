from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ActivityPage(BasePage):
    ACTIVITY_URL = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
                   "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
                   "eventTypes][0]=AUCTION_CREATED "
    ACTIVITY_TITLE = "Activity | OpenSea"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.ACTIVITY_URL)
