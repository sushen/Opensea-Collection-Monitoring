from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class BuyPage(BasePage):
    buy_button = (By.XPATH, "//button[contains(text(),'Buy now')]")
    accept_button = (By.XPATH, "//input[@id='tos']")
    example_nft_url = "https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/881756771131205292479386972198912303276944630623864784050108750075382464513"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.example_nft_url)

    def buy_button_click(self):
        self.do_click(self.buy_button)

    def accept_button_click(self):
        self.do_click(self.accept_button)
