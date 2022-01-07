import os
import runpy
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import re
import random
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

driver = webdriver.Chrome("/home/tawhid/Downloads/chromedriver/chromedriver", chrome_options=chrome_options)

link = "https://opensea.io/assets/0xc926d9b50fffbe9bc6db02362cc15f5a5f3b23c2/1222?fbclid" \
       "=IwAR1P68BBsBijGhL6l2pCb6sa8snpirVccBzRXQFiLhh9e0A0ydgoHTydDQU "


def buy_single_nft(nft_link):
    driver.get(nft_link)
    print(input("Connect Metamask  :"))

    for i in range(1000):
        driver.get(nft_link)
        # print(input("Go For Refresh  :"))
        driver.implicitly_wait(10)
        # driver.refresh()

        buy_button = "//button[contains(text(),'Buy now')]"
        driver.find_element_by_xpath(buy_button).click()
        # print(input("GO for Unreview :"))

        driver.implicitly_wait(10)

        unreview_nft = "//input[@id='review-confirmation']"
        driver.find_element_by_xpath(unreview_nft).click()
        # print(input("GO for Tos :"))

        driver.implicitly_wait(10)
        tos = "//input[@id='tos']"
        driver.find_element_by_xpath(tos).click()
        # print(input("Go For Conform checkout :"))

        driver.implicitly_wait(10)
        conform_checkout = "//button[.='Confirm checkout']"
        driver.find_element_by_xpath(conform_checkout).click()

        # print(input("Go For Metamask  :"))

        time.sleep(20)

        # TODO : go for Title conformation
        window_before = driver.window_handles[0]
        print(driver.title)
        print(window_before)

        driver.implicitly_wait(10)
        time.sleep(.5)
        window_after = driver.window_handles[1]
        # driver.switch_to_window(window_after)
        driver.switch_to.window(window_after)
        print(window_after)
        print(".......................")
        print(driver.title)

        # print(input("Go for edit balance : "))
        edit_transaction = "//button[.='Edit']"
        driver.find_element_by_xpath(edit_transaction).click()

        driver.implicitly_wait(10)
        time.sleep(4)

        # print(input("Go for advanced option : "))
        advanced_options = '//button[@class="edit-gas-display__advanced-button"]'
        driver.find_element_by_xpath(advanced_options).click()

        # print(input("Start form handling : "))
        gas_limit_numeric_input = '//div[@class="numeric-input"]'
        gas_limit_numeric_input_elements = driver.find_elements_by_xpath(gas_limit_numeric_input)
        print(gas_limit_numeric_input_elements)
        print(len(gas_limit_numeric_input_elements))
        print(gas_limit_numeric_input_elements[0])
        gas_limit_numeric_input_elements[0].click()

        # print(input("Send gas limit : "))

        action = ActionChains(driver)

        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL) \
            .send_keys(Keys.BACK_SPACE).send_keys(30000).perform()

        gas_limit_numeric_input_elements[1].click()

        # print(input("Send Max priority fee : "))
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL) \
            .send_keys(Keys.BACK_SPACE).send_keys(2).perform()

        gas_limit_numeric_input_elements[2].click()

        # print(input("Send max fee : "))

        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL) \
            .send_keys(Keys.BACK_SPACE).send_keys(100).perform()

        # print(input("Save and Reject :D  : "))
        save_btn = "//button[normalize-space()='Save']"
        driver.find_element_by_xpath(save_btn).click()
        time.sleep(1)
        reject_btn = "//button[normalize-space()='Reject']"
        driver.find_element_by_xpath(reject_btn).click()
        driver.switch_to.window(window_before)


buy_single_nft(link)
