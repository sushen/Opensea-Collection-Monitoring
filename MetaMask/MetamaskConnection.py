import os
import time


class MetaMask:

    def click_print_element(self, wallet_xpath, driver):
        print(f"inside {wallet_xpath}")
        # wallet_xpath = "//span[normalize-space()='MetaMask']"
        driver.implicitly_wait(10)
        wallet = driver.find_element_by_xpath(wallet_xpath)
        print(wallet)
        wallet.click()

    def connect_font_page_metamask(self, wallet_xpath, driver):
        self.click_print_element(wallet_xpath, driver)

    def download_metamask(self, wallet_xpath, driver):
        self.click_print_element(wallet_xpath, driver)

        # time.sleep(4)
        w_h = driver.window_handles

        # print(len(w_h))
        # print(w_h)

        if len(w_h) > 1:
            print(input("Downloader and Install Metamask \nRestart The Program again:"))

        else:
            pass

    def enter_metamask(self, wallet_xpath, driver):

        metamask_password = os.environ.get('metamask_password')

        self.click_print_element(wallet_xpath, driver)

        time.sleep(4)
        w_h = driver.window_handles

        print(len(w_h))
        print(w_h)

        if len(w_h) > 1:
            window_before = driver.window_handles[0]
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            window_after_title = driver.title
            print(window_after_title)
            self.click_print_element("//input[@class='MuiInputBase-input MuiInput-input']", driver)
            driver.find_element_by_xpath("//input[@class='MuiInputBase-input MuiInput-input']").send_keys(
                metamask_password)
            self.click_print_element("//button[@class='button btn--rounded btn-default']", driver)
            time.sleep(10)
            # print(input("Metamask Password:"))

            w_h = driver.window_handles
            print(len(w_h))
            print(w_h)

            if len(w_h) > 1:
                # self.click_print_element("//button[@class='button btn--rounded btn-primary']", driver)
                self.click_print_element(
                    "//button[@class='button btn--rounded btn-secondary page-container__footer-button']", driver)
                driver.switch_to.window(window_before)
                print(window_after_title)
            else:
                pass

            time.sleep(4)
            w_h = driver.window_handles
            print(len(w_h))
            print(w_h)

            if len(w_h) > 1:
                self.click_print_element("//button[@class='button btn--rounded btn-primary']", driver)
                self.click_print_element(
                    "//button[@class='button btn--rounded btn-primary page-container__footer-button']", driver)
                driver.switch_to.window(window_before)
                print(window_after_title)
            else:
                pass
            driver.switch_to.window(window_before)
            print(driver.title)

    def connect_metamask_first_time(self, driver):
        print("inside connect_metamask_first_time")
        driver.refresh()
        self.connect_font_page_metamask("//i[@title='Wallet']", driver)
        self.enter_metamask("//span[normalize-space()='MetaMask']", driver)
