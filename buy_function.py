




def buy_single_nft():
    buy_button = "//button[contains(text(),'Buy now')]"
    driver.find_element_by_xpath(buy_button).click()
    driver.implicitly_wait(10)
    # unreviewed_nft_path = "//input[@id='review-confirmation']"
    # driver.find_element_by_xpath(unreviewed_nft_path)
    driver.implicitly_wait(10)
    tos = "//input[@id='tos']"
    driver.find_element_by_xpath(tos).click()
    driver.implicitly_wait(10)
    conform_checkout = "//button[.='Confirm checkout']"
    driver.find_element_by_xpath(conform_checkout).click()
    time.sleep(20)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    edit_transaction = "//button[.='Edit']"
    driver.find_element_by_xpath(edit_transaction).click()
    driver.implicitly_wait(10)
    time.sleep(4)
    advanced_options = '//button[@class="edit-gas-display__advanced-button"]'
    driver.find_element_by_xpath(advanced_options).click()
    gas_limit_numeric_input = '//div[@class="numeric-input"]'
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
    save_btn = "//button[normalize-space()='Save']"
    driver.find_element_by_xpath(save_btn).click()
    time.sleep(1)
    reject_btn = "//button[normalize-space()='Reject']"
    driver.find_element_by_xpath(reject_btn).click()
    driver.switch_to.window(window_before)
