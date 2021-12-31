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
NFT_link = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
           "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
           "eventTypes][0]=AUCTION_CREATED "

login_link = "https://opensea.io/login?referrer=%2Faccount"

# This is for Single Buy Button
buy_xpath = "//button[normalize-sppace()='Buy Now']"

driver = webdriver.Chrome(r"../opensea/chromedriver.exe", chrome_options=chrome_options)

# User must log in before running code
# driver.implicitly_wait(10)

# driver.get(login_link)

# print(input("Connect wallet, then hit enter >>>>>> "))

driver.implicitly_wait(10)
driver.get(NFT_link)

# paths variables
accept_xpath = "//input[@id='tos']"
time_xpath = "//div[@data-testid='EventTimestamp']"
nft_names_xpath = "//div[@role='listitem']//child::div[@class='AssetCell--container']"
nft_price_xpath = "//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--fiat-amount']"
nft_click_xpath = "//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq styles__CoverLink-sc-nz4knd-1 givILt']"
buy_button_path = "//button[contains(text(),'Buy now')]"
floor_prices_xpath = "//a[@class='chakra-link css-166ifkv']"
nft_eth_price_xpath = "//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--amount']"

expected_price = 300000
expected_time = 59

for i in range(100):
    # driver.refresh()
    driver.get(NFT_link)
    driver.implicitly_wait(10)
    time.sleep(.1)
    nft_names = driver.find_elements_by_xpath(nft_names_xpath)
    # time_elements = driver.find_elements_by_xpath(time_xpath)
    # nft_prices = driver.find_elements_by_xpath(nft_price_xpath)
    nft_click = driver.find_elements_by_xpath(nft_click_xpath)

    nft_eth_prices = driver.find_elements_by_xpath(nft_eth_price_xpath)

    # Getting first nft and it's details
    nft_name = nft_names[-1].text
    # time_text = time_elements[-1].text
    # nft_price = nft_prices[-1].text

    nft_eth_price = nft_eth_prices[-1].text

    # Ignore all numbers after . because it causes error
    separator = '.'
    # separated_price = nft_price.split(separator, 1)[0]

    # Remove special characters from price and time variable
    # price_stripped = re.sub("[^0-9]", "", separated_price)
    # time_stripped = re.sub("[^0-9]", "", time_text)
    # //div[@class='SuperSea__AssetInfo SuperSea__AssetInfo--list']//child::a[@class='chakra-link css-166ifkv']

    driver.implicitly_wait(10)
    time.sleep(4)
    nft_token = re.sub("[^0-9]", "", nft_name)
    nft_floor_price_xpath = f"//div[@data-token-id='{nft_token}']//child::a[@class='chakra-link css-166ifkv']"
    nft_floor_price = driver.find_element_by_xpath(nft_floor_price_xpath).text

    print(f"NFT name is: -- {nft_name}\n"
          f"NFT current price is: -- {nft_eth_price}\n"
          f"NFT floor price is: -- {nft_floor_price}\n")

    if float(nft_floor_price) > float(nft_eth_price):
        nft_click[-1].click()
        print('Matched!')
        buy_button = driver.find_element_by_xpath(buy_button_path)
        if buy_button:
            buy_button.click()
            print('Button clicked!')

            accept_input = driver.find_element_by_xpath(accept_xpath)
            accept_input.click()
            print(input('>>>>>>> '))
            print("Terms accepted")
            time.sleep(4)

    else:
        print("\nPrice or Time is greater than expectation, Trying again...")
        time.sleep(6)

# TODO : Compare floor price to price and Make buy when floor price is lover than original price

# TODO : Install extension
