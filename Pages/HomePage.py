from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """ constructor of the page class """

    """ By Locators - OR  """
    PASSWORD = (By.ID, "pass")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
