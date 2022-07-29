# TODO : Go to Base Website - https://opensea.io/
import os
import time
from Bots.bot_ActivityPage import BotActivityPage
from Bots.bot_BuyPage import BotBuyPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

metamask_password = os.environ.get('metamask_password')

buy_page = BotBuyPage()


def conform_perches(driver):
    # print(input("conform :"))

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
    # print(input("metamask :"))

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


def click_print_element(wallet_xpath):
    print(f"inside {wallet_xpath}")
    # wallet_xpath = "//span[normalize-space()='MetaMask']"
    buy_page.driver.implicitly_wait(10)
    wallet = buy_page.driver.find_element_by_xpath(wallet_xpath)
    print(wallet)
    wallet.click()


def connect_font_page_metamask(wallet_xpath):
    click_print_element(wallet_xpath)


def download_metamask(wallet_xpath):
    click_print_element(wallet_xpath)

    # time.sleep(4)
    w_h = buy_page.driver.window_handles

    # print(len(w_h))
    # print(w_h)

    if len(w_h) > 1:
        print(input("Downloader and Install Metamask \nRestart The Program again:"))

    else:
        pass


def enter_metamask(wallet_xpath):
    click_print_element(wallet_xpath)

    time.sleep(4)
    w_h = buy_page.driver.window_handles

    print(len(w_h))
    print(w_h)

    if len(w_h) > 1:
        window_before = buy_page.driver.window_handles[0]
        window_after = buy_page.driver.window_handles[1]
        buy_page.driver.switch_to.window(window_after)
        window_after_title = buy_page.driver.title
        print(window_after_title)
        click_print_element("//input[@class='MuiInputBase-input MuiInput-input']")
        buy_page.driver.find_element_by_xpath("//input[@class='MuiInputBase-input MuiInput-input']").send_keys(metamask_password)
        click_print_element("//button[@class='button btn--rounded btn-default']")
        time.sleep(10)
        # print(input("Metamask Password:"))

        w_h = buy_page.driver.window_handles
        print(len(w_h))
        print(w_h)

        if len(w_h) > 1:
            click_print_element("//button[@class='button btn--rounded btn-primary']")
            click_print_element("//button[@class='button btn--rounded btn-primary page-container__footer-button']")
            buy_page.driver.switch_to.window(window_before)
            print(window_after_title)
        else:
            pass
        buy_page.driver.switch_to.window(window_before)


def connect_metamask_first_time():
    print("inside connect_metamask_first_time")
    buy_page.driver.refresh()
    connect_font_page_metamask("//i[@title='Wallet']")
    enter_metamask("//span[normalize-space()='MetaMask']")


connect_font_page_metamask("//i[@title='Wallet']")
download_metamask("//span[normalize-space()='MetaMask']")
connect_metamask_first_time()


time.sleep(10)
buy_page.driver.quit()

