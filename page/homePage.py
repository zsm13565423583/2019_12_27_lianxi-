from selenium.common.exceptions import TimeoutException

from base.base import Base
from page.pageElements import PageElements


class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_after_btn(self):
        try:
            self.click_ele(PageElements.home_after_btn_id)
        except TimeoutException:
            print("更新弹窗没有弹出")

    def click_my_btn(self):
        self.click_ele(PageElements.home_my_btn_id)
