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

driver = webdriver.Chrome(r"../opensea/chromedriver.exe", chrome_options=chrome_options)

link = "https://opensea.io/assets/0xc926d9b50fffbe9bc6db02362cc15f5a5f3b23c2/1222?fbclid" \
       "=IwAR1P68BBsBijGhL6l2pCb6sa8snpirVccBzRXQFiLhh9e0A0ydgoHTydDQU "

details_x = "//span[contains(normalize-space(),'Details')]/ancestor::button"
contract_address_x = "//div[contains(text(),'Contract Address')]//a"
contract_x = "//a[@href='#contracts']//span[contains(text(),'Contract')]"

write_contract_x = "//a[@href='#writeContract']"
mint_x = "//a[normalize-space()='2. mint']"

input_1 = "//input[@name='payable_mint']"
input_2 = "//input[@name='input_2']"

action = ActionChains(driver)

for i in range(100):
    driver.get(link)
    driver.implicitly_wait(10)
    time.sleep(5)

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)

    driver.find_element_by_xpath(details_x).click()
    time.sleep(1)
    driver.find_element_by_xpath(contract_address_x).click()

    time.sleep(5)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_xpath(contract_x).click()
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_xpath(write_contract_x).click()
    driver.implicitly_wait(10)
    time.sleep(5)

    driver.switch_to.frame("writecontractiframe")
    time.sleep(5)
    driver.find_element_by_xpath(mint_x).click()
    time.sleep(5)
    driver.switch_to.window(window_before)
