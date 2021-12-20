import os
import runpy
import time


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# For Sound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 2500  # Set Duration To 1000 ms == 1 second

# Setting the chrome_options
global chrome_options
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

# TODO: How much you want to buy
buying_limits = 10

# TODO: You need to put your NFT link here
NFT_link = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[eventTypes][0]=AUCTION_CREATED"

# This is for Single Buy Button
buy_xpath = "//button[normalize-sppace()='Buy Now']"

driver = webdriver.Chrome(r"../opensea/chromedriver.exe", chrome_options=chrome_options)

# print(input(" Connect your waller address :"))
driver.implicitly_wait(10)
driver.get(NFT_link)

# TODO: Filter
