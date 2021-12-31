from Bots.bot_base import BaseBot

from Pages.BuyPage import BuyPage


class BotBuyPage(BaseBot):
    def test_buy_button(self):
        self.buy_page = BuyPage(self.driver)
        self.buy_page.buy_nft()

