# from selenium.webdriver.common.by import By

# from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ActivityPage(BasePage):
    ACTIVITY_URL = "https://opensea.io/activity"
    ACTIVITY_TITLE = "Activity | OpenSea"

    # ACTIVITY_ITEM = (By.XPATH, "//div[12]//button[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[2]//span[2]//a[1]")

    ETH_PRICE = (By.XPATH, "//div[@role='list']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.ACTIVITY_URL)

    '''def activity_item_button_click(self):
        self.do_click(self.ACTIVITY_ITEM)'''

    def eth_price_button_click(self):
        self.do_click(self.ETH_PRICE)

# //div[@class='SearchPills react__DivContainer-sc-1djjvtl-0 bxyEMq SearchPills--hasContent']
# (//div[@class='SearchPills react__DivContainer-sc-1djjvtl-0 bxyEMq SearchPills--hasContent'])[1]

# /html/body/div[1]/div[1]/div/main/div/div[1]/div/div[3]/div[2]/div/div/div[7]/button/div/div/div/div[2]/div/div/div[1]/a/div/img
