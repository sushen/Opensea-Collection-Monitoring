import time

import pyautogui as pyautogui
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


# url = "https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/881756771131205292479386972198912303276944630623864784050108750075382464513"
# url = "https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/31097931735536228284032699637255406190173055095304977551590049585738280861946/"
url = "https://opensea.io/assets/ethereum/0x0b3b95547a22bee3c03be558ec649dbd69af8476/3307"

extension_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"


class BuyNft(BasePage):

    def buy_button_click(self, buy_button):
        self.do_click(buy_button)


from OpenseaBusinessLogic.driver import Driver
dr = Driver()
buy_nft = BuyNft(dr.driver)
dr.driver.get("https://opensea.io")

from MetaMask.MetamaskConnection import MetaMask
mm = MetaMask()
mm.connect_font_page_metamask("//i[@title='Wallet']", dr.driver)
mm.download_metamask("//span[normalize-space()='MetaMask']", dr.driver)
mm.connect_metamask_first_time(dr.driver)

dr.driver.get(url)
dr.driver.refresh()
buy_nft.do_click((By.XPATH, "//button[contains(text(),'Buy now')]"))
buy_nft.do_click((By.XPATH, "//span[normalize-space()='Complete purchase']"))
# buy_nft.driver.switch_to.new_window()
buy_nft.new_browder_tab(extension_url)
# dr.driver.get(extension_url)

w_h = dr.driver.window_handles

print(len(w_h))
print(w_h)

from MetaMask.MetamaskBody import MetamaskBody
mmb = MetamaskBody(dr.driver)
mmb.fulfill_basic_order()
dr.driver.close()
dr.driver.switch_to.window(dr.driver.window_handles[0])

w_h = dr.driver.window_handles

print(len(w_h))
print(w_h)

print(input(".."))


buy_nft.do_click((By.XPATH, "//button[normalize-space()='Continue']"))
buy_nft.do_click((By.XPATH, "//input[@id='review-confirmation']"))
