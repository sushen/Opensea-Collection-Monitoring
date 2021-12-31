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

link = "https://opensea.io/assets/0xc926d9b50fffbe9bc6db02362cc15f5a5f3b23c2/1222?fbclid=IwAR1P68BBsBijGhL6l2pCb6sa8snpirVccBzRXQFiLhh9e0A0ydgoHTydDQU"

driver.get(link)
print(input("Go For Refresh  :"))

driver.implicitly_wait(10)
driver.refresh()

print(input("Connect Metamask  :"))
# TODO : Here we find problem connected metamask
# driver.implicitly_wait(10)
# connect_metamask = "i[title='Wallet']"
# wallet_element = driver.find_element_by_xpath(connect_metamask)
# print(wallet_element)
# print(wallet_element.text)
# print(input("Connect Metamask Done :"))

buy_button = "//button[contains(text(),'Buy now')]"
driver.find_element_by_xpath(buy_button).click()
print(input("GO for Unreview :"))

driver.implicitly_wait(10)

unreview_nft = "//input[@id='review-confirmation']"
driver.find_element_by_xpath(unreview_nft).click()
print(input("GO for Tos :"))

driver.implicitly_wait(10)
tos = "//input[@id='tos']"
driver.find_element_by_xpath(tos).click()
print(input("Go For Conform checkout :"))

driver.implicitly_wait(10)
conform_checkout = "//button[.='Confirm checkout']"
driver.find_element_by_xpath(conform_checkout).click()
print(input("Go For Metamask  :"))

# TODO : go for Title conformation
window_before = driver.window_handles[0]
print(driver.title)
print(window_before)


driver.implicitly_wait(10)
time.sleep(4)
window_after = driver.window_handles[1]
# driver.switch_to_window(window_after)
driver.switch_to.window(window_after)
print(window_after)
print(".......................")
print(driver.title)

edit_transaction = "//button[.='Edit']"
driver.find_element_by_xpath(edit_transaction).click()

driver.implicitly_wait(10)
time.sleep(4)

advanced_options = "//button[.='Advanced Options']"
driver.find_element_by_xpath(advanced_options).click()

