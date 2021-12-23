import os
import runpy
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pathlib
import re
import random

# from bs4 import BeautifulSoup


# For Sound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 2500  # Set Duration To 1000 ms == 1 second

# Setting the chrome_options
global chrome_options
chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--profile-directory=Profile 8")
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")

# for windows uncomment below line

chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

# TODO: How much you want to buy
buying_limits = 10

# TODO: You need to put your NFT link here
NFT_link = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
           "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
           "eventTypes][0]=AUCTION_CREATED "

# This is for Single Buy Button
buy_xpath = "//button[normalize-sppace()='Buy Now']"




#windows setup
# driver = webdriver.Chrome(r"../opensea/chromedriver.exe", chrome_options=chrome_options)

# linx setup
driver = webdriver.Chrome(r"./chromedriver", chrome_options=chrome_options)

# print(input(" Connect your waller address :"))
driver.implicitly_wait(10)
driver.get(NFT_link)
# driver.implicitly_wait(10)
# class="Navbar--brand-name"
# undefined
driver.implicitly_wait(5)
# element = driver.find_element_by_class_name("Navbar--brand-name")
element = driver.find_element_by_css_selector("div[data-testid='EventTimestamp']")

print(element.text.split(" ")[0])
upload_time = element.text.split(" ")
print(upload_time[0],upload_time[1])
if (
    (upload_time[0] != "a"
    and upload_time[1].lower() != "minute")
    or upload_time[1].lower() != "minutes" or upload_time[1].lower() != "minute"
    or (upload_time[0] == "a" and upload_time[1].lower() == "second")
):
    second_time = upload_time[0]
    if ((second_time == "a" and upload_time[1].lower() != "minute")  or (second_time != "a" and int(second_time) <= 20) and upload_time[1].lower() == "seconds"):
        p = element.find_element_by_xpath("..")
        p = p.find_element_by_xpath("..")
        n = p.find_element_by_class_name("AssetCell--link")
        # print(n.get_attribute("class"))
        # print(n.get_attribute("href"))
        driver.get("https://opensea.io" + n.get_attribute("href"))

        # button = driver.find_element_by_link_text('Buy now')
        button = driver.find_element_by_xpath("//button[contains(text(), 'Buy now')]")

        # find_element_by_xpath("//button[@='link']")
        print(button.get_attribute("class"))
        driver.implicitly_wait(5)
        button.send_keys("\n")
        time.sleep(4)


# print(k.text)
# k.click()

driver.implicitly_wait(20)


driver.quit()

# <a class="styles__StyledLink-sc-l6elh8-0 ekTmzq EventTimestamp--link" href="https://polygonscan.com/tx/0xe4e49eb43c34e0210e95db8e9ab6ee863a01ec8ea5298e438eb62be4009d53bb" rel="nofollow noopener" target="_blank" aria-expanded="false">37 seconds ago <i class="Iconreact__Icon-sc-1gugx8q-0 irnoQt EventTimestamp--link-icon material-icons EventTimestamp--link-icon" value="open_in_new" size="24">open_in_new</i></a>
# <a class="styles__StyledLink-sc-l6elh8-0 ekTmzq EventTimestamp--link" href="https://etherscan.io/tx/0x4e896ece1b4fb832615c5a22a330a14f05810e84a1b7ec2224ed38c4738b68fe" rel="nofollow noopener" target="_blank" aria-expanded="false">a minute ago <i class="Iconreact__Icon-sc-1gugx8q-0 irnoQt EventTimestamp--link-icon material-icons EventTimestamp--link-icon" value="open_in_new" size="24">open_in_new</i></a>
# <a class="styles__StyledLink-sc-l6elh8-0 ekTmzq EventTimestamp--link" href="https://etherscan.io/tx/0x739f11c3557197630aa41c59f6057582e001f85158e78bcf221984697d51994a" rel="nofollow noopener" target="_blank" aria-expanded="false">4 minutes ago <i class="Iconreact__Icon-sc-1gugx8q-0 irnoQt EventTimestamp--link-icon material-icons EventTimestamp--link-icon" value="open_in_new" size="24">open_in_new</i><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq EventTimestamp--link" href="https://etherscan.io/tx/0x4e896ece1b4fb832615c5a22a330a14f05810e84a1b7ec2224ed38c4738b68fe" rel="nofollow noopener" target="_blank" aria-expanded="false">2 minutes ago <i class="Iconreact__Icon-sc-1gugx8q-0 irnoQt EventTimestamp--link-icon material-icons EventTimestamp--link-icon" value="open_in_new" size="24">open_in_new</i></a></a>

# TODO: Filter Price

# Setting paths and variables

time_xpath = "//div[@data-testid='EventTimestamp']"
nft_names_xpath = "//div[@role='listitem']//child::div[@class='AssetCell--container']"
nft_price_xpath = "//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--fiat-amount']"
nft_click_xpath = "//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq styles__CoverLink-sc-nz4knd-1 givILt']"
buy_button_path = "//button[contains(text(),'Buy now')]"

expected_price = 30000
expected_time = 59

nft_names = driver.find_elements_by_xpath(nft_names_xpath)
time_elements = driver.find_elements_by_xpath(time_xpath)
nft_prices = driver.find_elements_by_xpath(nft_price_xpath)
nft_click = driver.find_elements_by_xpath(nft_click_xpath)

# TODO: Find Single NFT

# Getting first nft and it's details
nft_name = nft_names[-1].text
time_text = time_elements[-1].text
nft_price = nft_prices[-1].text

# Ignore all numbers after . because it causes error
separator = '.'
separated_price = nft_price.split(separator, 1)[0]

# Remove special characters from price and time variable
price_stripped = re.sub("[^0-9]", "", separated_price)
time_stripped = re.sub("[^0-9]", "", time_text)

# Check if optimal conditions are met or not
print(f"\ntime: {time_stripped}, price: {price_stripped}")
if float(price_stripped) < expected_price and int(time_stripped) < expected_time:
    nft_click[-1].click()
    print('Matched!')
    buy_button = driver.find_element_by_xpath(buy_button_path)
    if buy_button:
        buy_button.click()
        print('Button clicked!')

