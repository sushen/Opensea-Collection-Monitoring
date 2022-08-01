import time
from selenium.webdriver.common.by import By
from OpenseaBusinessLogic.driver import Driver
from Pages.BasePage import BasePage


extension_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
collection_url = "https://opensea.io/collection/thepotatoz"


class SearchCollection(BasePage):
    def find_floor_price(self):
        return self.get_element_text(
            (By.XPATH, "(//div[@class='sc-1xf18x6-0 sc-1twd32i-0 iQOhGx kKpYwv'][normalize-space()])[9]"))

    def select_nft(self):
        # path = "(//div[@role='gridcell'])[1]"
        self.do_click((By.XPATH, "(//div[@role='gridcell'])[1]"))


dr = Driver()
dr.driver.get("https://opensea.io")

from MetaMask.MetamaskConnection import MetaMask
mm = MetaMask()
mm.connect_font_page_metamask("//i[@title='Wallet']", dr.driver)
mm.download_metamask("//span[normalize-space()='MetaMask']", dr.driver)
mm.connect_metamask_first_time(dr.driver)

dr.driver.get(collection_url)


sc = SearchCollection(dr.driver)

buying_floor_price = 1.29

for i in range(100):
    print(f"Current Floor Price :{sc.find_floor_price()}")
    if float(sc.find_floor_price()) <= buying_floor_price:
        sc.select_nft()
        sc.do_click((By.XPATH, "//button[contains(text(),'Buy now')]"))
        sc.do_click((By.XPATH, "//span[normalize-space()='Complete purchase']"))
        sc.new_browder_tab(extension_url)

        from MetaMask.MetamaskBody import MetamaskBody
        from email_option import email_paramiter

        mmb = MetamaskBody(dr.driver)
        mmb.fulfill_basic_order()
        dr.driver.close()
        dr.driver.switch_to.window(dr.driver.window_handles[0])

        from email_option.sending_mail import MailSender
        from email_option.ip_address import IpAddress
        from email_option import mac_address
        sender1 = MailSender()
        sender1.login()
        sender1.send_mail(email_paramiter.gmail, f"Open Sea Collection Purchase Successful : IP {IpAddress().ip_address()} and MAC:{mac_address.mac_address}", f"We buy :{float(sc.find_floor_price())} eth")
        break

    else:
        print(f"Current Floor Price :{sc.find_floor_price()} Searching Below {buying_floor_price}")
        dr.driver.refresh()

    time.sleep(2)



