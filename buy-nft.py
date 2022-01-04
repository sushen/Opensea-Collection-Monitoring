import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib

from selenium.webdriver.common.keys import Keys
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

# paths variables
login_link = "https://opensea.io/login?referrer=%2Faccount"
NFT_link = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
           "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
           "eventTypes][0]=AUCTION_CREATED "
nft_names_xpath = "//div[@role='listitem']//child::div[@class='AssetCell--container']"
nft_click_xpath = "//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq styles__CoverLink-sc-nz4knd-1 givILt']"
floor_prices_xpath = "//div[@class='AssetCell--container']//child::a[@class='chakra-link css-166ifkv']"
nft_eth_price_xpath = "//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--amount']"
tos = "//input[@id='tos']"
buy_button = "//button[contains(text(),'Buy now')]"
confirm_checkout = "//button[.='Confirm checkout']"
edit_transaction = "//button[.='Edit']"
advanced_options = '//button[@class="edit-gas-display__advanced-button"]'
gas_limit_numeric_input = '//div[@class="numeric-input"]'
save_btn = "//button[normalize-space()='Save']"
reject_btn = "//button[normalize-space()='Reject']"

driver.get(login_link)
print(input("Connect Metamask >>>>> "))
start_time = time.time()
print("Script started at - " + time.ctime())

for i in range(100):
    driver.get(NFT_link)
    time.sleep(1)
    driver.implicitly_wait(10)
    nft_names = driver.find_elements_by_xpath(nft_names_xpath)
    single_nft = driver.find_elements_by_xpath(nft_click_xpath)
    nft_prices = driver.find_elements_by_xpath(nft_eth_price_xpath)

    nft_name = nft_names[-1].text
    nft_price = nft_prices[-1].text

    time.sleep(4)
    nft_floor_prices = driver.find_elements_by_xpath(floor_prices_xpath)
    nft_floor_price = nft_floor_prices[-1].text

    print(f"NFT name : {nft_name}\n"
          f"NFT price : {nft_price}\n"
          f"NFT floor price : {nft_floor_price}\n")

    if float(nft_floor_price) < float(nft_price):
        single_nft[-1].click()
        time.sleep(5)

        driver.find_element_by_xpath(buy_button).click()
        driver.implicitly_wait(10)

        driver.find_element_by_xpath(tos).click()
        driver.implicitly_wait(10)

        driver.find_element_by_xpath(confirm_checkout).click()
        time.sleep(20)

        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        driver.find_element_by_xpath(edit_transaction).click()
        driver.implicitly_wait(10)
        time.sleep(4)
        driver.find_element_by_xpath(advanced_options).click()

        gas_limit_numeric_input_elements = driver.find_elements_by_xpath(gas_limit_numeric_input)
        gas_limit_numeric_input_elements[0].click()
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL) \
            .send_keys(Keys.BACK_SPACE).send_keys(30000).perform()
        gas_limit_numeric_input_elements[1].click()
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL) \
            .send_keys(Keys.BACK_SPACE).send_keys(2).perform()
        gas_limit_numeric_input_elements[2].click()
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL) \
            .send_keys(Keys.BACK_SPACE).send_keys(100).perform()
        driver.find_element_by_xpath(save_btn).click()
        time.sleep(1)
        driver.find_element_by_xpath(reject_btn).click()
        driver.switch_to.window(window_before)
        time.sleep(10)

    else:
        print("No NFT found, Trying again....")
        time.sleep(5)

total_run_time = (time.time() - start_time)
print(f"This script was running for {total_run_time}")
