from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_BasePage import BaseTest

from Pages.ActivityPage import ActivityPage


class TestActivityPage(BaseTest):
    def test_home_title(self):
        self.activity_page = ActivityPage(self.driver)
        title = self.activity_page.get_title(ActivityPage.ACTIVITY_TITLE)
        assert title == ActivityPage.ACTIVITY_TITLE



