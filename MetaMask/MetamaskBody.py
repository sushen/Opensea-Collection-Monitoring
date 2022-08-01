from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class MetamaskBody(BasePage):

    def fulfill_basic_order(self):
        self.do_click((By.XPATH, "//h2[contains(text(),' Fulfill  Basic  Order')]"))
        self.do_click((By.XPATH, "//span[contains(text(),'Site suggested')]"))
        self.do_click((By.XPATH, "//span[@class='edit-gas-item__icon edit-gas-item__icon-custom']"))
        self.do_click((By.XPATH, "//a[@class='button btn-link advanced-gas-fee-gas-limit__edit-link']"))

        # Edit Gash Limit if necessary
        self.do_click((By.XPATH, "//input[@data-testid='gas-limit-input']"))
        self.do_select_keys()
        self.do_send_keys((By.XPATH, "//input[@data-testid='gas-limit-input']"), '160013')

        self.do_click((By.XPATH, "//button[@class='button btn--rounded btn-primary']"))

        # Buy Rela NFT
        print(input("Process Payment"))
        # self.do_click((By.XPATH, "//button[contains(text(),'Confirm')]"))
        self.do_click((By.XPATH, "//button[@class='button btn--rounded btn-secondary page-container__footer-button']"))

        print("Order Conformed")



