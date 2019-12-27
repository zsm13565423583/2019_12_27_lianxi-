from base.base import Base
from page.pageElements import PageElements


class PersonPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_login_sigin_btn(self):
        self.click_ele(PageElements.person_login_sigin_btn_xpath)

    def get_username(self):
        return self.search_ele(PageElements.person_user_name_id).text

    def click_setting_btn(self,tag=1):
        #点击设置
        #向上滑动
        self.swipe_screen()
        #点击设置按钮
        self.click_ele(PageElements.person_setting_btn_id)
