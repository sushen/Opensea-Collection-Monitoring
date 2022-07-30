"""
Commend run in terminal
pytest Tests/test_BuyPage.py
python -m pytest
"""
from OpenseaBusinessLogic.MetamaskConnection import MetaMask
from Tests.test_BasePage import BaseTest

from Pages.BuyPage import BuyPage


class TestBuyPage(BaseTest):

    def metamask_connection(self):
        # print("Connect Wallet")
        mm = MetaMask()
        mm.connect_font_page_metamask("//i[@title='Wallet']", self.driver)
        mm.download_metamask("//span[normalize-space()='MetaMask']", self.driver)
        mm.connect_metamask_first_time(self.driver)
        print(input("Connect Wallet"))

    def test_buy_button(self):
        self.buy_page = BuyPage(self.driver)
        self.metamask_connection()
        self.buy_page.do_click(self.buy_page.buy_button)

    # def test_accept_button(self):
    #     self.buy_page = BuyPage(self.driver)
    #     self.buy_page.do_click(self.buy_page.accept_button)



