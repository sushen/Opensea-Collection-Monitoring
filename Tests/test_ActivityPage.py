from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_BasePage import BaseTest

from Pages.ActivityPage import ActivityPage


class TestActivityPage(BaseTest):
    def test_home_title(self):
        self.activity_page = ActivityPage(self.driver)
        title = self.activity_page.get_title(ActivityPage.ACTIVITY_TITLE)
        assert title == ActivityPage.ACTIVITY_TITLE

    def test_get_first_nft_name(self):
        self.activity_page = ActivityPage(self.driver)
        self.activity_page.get_first_nft_name(ActivityPage.NFT_NAMES)

    # def test_get_first_nft_price(self):
    #     self.activity_page = ActivityPage(self.driver)
    #     first_nft_price = self.activity_page.get_first_nft_price(self.driver)
    #     print(first_nft_price)
