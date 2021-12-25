import time

from Bots.bot_base import BaseBot

from Pages.ActivityPage import ActivityPage


class BotActivityPage(BaseBot):
    def test_home_title(self):
        self.activity_page = ActivityPage(self.driver)
        title = self.activity_page.get_title(ActivityPage.ACTIVITY_TITLE)
        print(title)
        assert title == ActivityPage.ACTIVITY_TITLE

    def test_get_first_nft_name(self):
        self.activity_page = ActivityPage(self.driver)
        self.activity_page.get_first_nft_name(ActivityPage.NFT_NAMES)


