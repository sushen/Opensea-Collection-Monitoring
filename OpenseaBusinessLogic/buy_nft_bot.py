# TODO : Go to Base Website - https://opensea.io/
import time
from Bots.bot_ActivityPage import BotActivityPage
from Bots.bot_BuyPage import BotBuyPage

# xpath variables
nft_eth_price_xpath = "//div[@class='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--amount']"
nft_names_xpath = "//div[@role='listitem']//child::div[@class='AssetCell--container']"
floor_prices_xpath = "//a[@class='chakra-link css-166ifkv']"
nft_click_xpath = "//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq styles__CoverLink-sc-nz4knd-1 givILt']"
ACTIVITY_URL = "https://opensea.io/activity?search[collections][0]=clonex&search[collections][" \
               "1]=boredapeyachtclub&search[collections][2]=dinobabies&search[collections][3]=coolmans-universe&search[" \
               "eventTypes][0]=AUCTION_CREATED "

buy_button = "//button[contains(text(),'Buy now')]"
tos_button = "//input[@id='tos']"


buy_page = BotBuyPage()


def conform_perches(driver):
    print(input(" :"))

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


def conform_metamask(driver):
    print(input(" :"))

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



buy_page.driver.get("https://opensea.io/")
print(input("Connect metamask:"))

for i in range(1000):
    buy_page.driver.get(ACTIVITY_URL)
    buy_page.driver.implicitly_wait(10)
    time.sleep(4)
    # print(input("Wating to load nft, this will be excluded later >>>> "))

    nft_names = buy_page.driver.find_elements_by_xpath(nft_names_xpath)
    nft_name = nft_names[-1].text

    nft_eth_prices = buy_page.driver.find_elements_by_xpath(nft_eth_price_xpath)
    nft_eth_price = nft_eth_prices[-1].text

    nft_floor_prices = buy_page.driver.find_elements_by_xpath(floor_prices_xpath)
    nft_floor_price = nft_floor_prices[-1].text

    print(f"NFT name : {nft_name} \n"
          f"NFT price in eth : {nft_eth_price} \n"
          f"NFT floor price : {nft_floor_price} \n")

    if float(nft_floor_price) < float(nft_eth_price):
        nft_click = buy_page.driver.find_elements_by_xpath(nft_click_xpath)
        nft_click[-1].click()
        # buy_page.test_buy_button()
        # TODO : Start The repeat loop and Continue...

        conform_perches(buy_page.driver)

        conform_metamask(buy_page.driver)




