import time

from selenium import webdriver

driver = webdriver.Chrome("../chromedriver.exe")

driver.get(
    "https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/31097931735536228284032699637255406190173055095304977551590049585738280861946/")

time.sleep(10)
driver.find_element_by_xpath("//button[contains(text(),'Buy now')]").click()
