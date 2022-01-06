import os
import runpy
import time

import winsound

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import re
import random
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

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
       # "=IwAR1P68BBsBijGhL6l2pCb6sa8snpirVccBzRXQFiLhh9e0A0ydgoHTydDQU "

#link = "https://opensea.io/assets/0xf9d53e156fe880889e777392585feb46d8d840f6/4745"


driver.get(link)
driver.implicitly_wait(10)
buy_button_xpath = "//button[contains(text(),'Buy now')]"
place_bid_xpath = "//button[contains(text(),'Place bid')]"

buy_button = driver.find_elements_by_xpath(buy_button_xpath)
place_bid = driver.find_elements_by_xpath(place_bid_xpath)



print(input('Wait untill load : '))
winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)

if driver.find_elements_by_xpath(buy_button_xpath)[0].click():
    print('Buy button')
elif driver.find_elements_by_xpath(place_bid_xpath)[0].click():
    print("Place bid")

else:
    print("Nothing found")