from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class BuyPage(BasePage):
    buy_button = (By.XPATH, "//button[contains(text(),'Buy now')]")
    by_checking_button = (By.XPATH, "//input[@id='tos']")
    example_nft_url = "https://opensea.io/assets/0xe8fc1aca7da14afb85182c113120896ac7c98a8a/7"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.example_nft_url)

    def buy_button_click(self):
        self.do_click(self.buy_button)

    def accept_button_click(self):
        self.do_click(self.by_checking_button)





# https://opensea.io/assets/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/11912
