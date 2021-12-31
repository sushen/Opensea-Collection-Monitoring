from selenium.webdriver.common.by import By
from Tests.test_BasePage import BaseTest

from Pages.BuyPage import BuyPage


class TestBuyPage(BaseTest):
    def test_buy_button(self):
        self.buy_page = BuyPage(self.driver)
        self.buy_page.do_click(self.buy_page.buy_button)



