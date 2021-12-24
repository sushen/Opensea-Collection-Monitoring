from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_BasePage import BaseTest


class TestHomePage(BaseTest):
    def test_home_title(self):
        self.homepage = HomePage(self.driver)
        title = self.homepage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE


