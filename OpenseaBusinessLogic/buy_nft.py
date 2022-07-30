from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


url = "https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/881756771131205292479386972198912303276944630623864784050108750075382464513"


class BuyNft(BasePage):

    def buy_button_click(self, buy_button):
        self.do_click(buy_button)


from OpenseaBusinessLogic.driver import Driver
dr = Driver()
buy_nft = BuyNft(dr.driver)
dr.driver.get("https://opensea.io")

from OpenseaBusinessLogic.MetamaskConnection import MetaMask
mm = MetaMask()
mm.connect_font_page_metamask("//i[@title='Wallet']", dr.driver)
mm.download_metamask("//span[normalize-space()='MetaMask']", dr.driver)
mm.connect_metamask_first_time(dr.driver)

# print(input(".."))
dr.driver.get(url)
buy_nft.do_click((By.XPATH, "//button[contains(text(),'Buy now')]"))
buy_nft.do_click((By.XPATH, "//input[@id='review-confirmation']"))
buy_nft.do_click((By.XPATH, "//span[normalize-space()='Complete purchase']"))
