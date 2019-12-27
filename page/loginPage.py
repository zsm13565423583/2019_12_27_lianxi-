from base.base import Base
from page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, phone,password):
        self.send_ele(PageElements.login_phone_id, phone)
        self.send_ele(PageElements.login_passwd_id, password)
        self.click_ele(PageElements.login_btn_id)

    def click_login_acc_btn(self):
        self.click_ele(PageElements.login_suc_acc_btn_id)

    def click_return_btn(self):
        self.click_ele(PageElements.login_return_btn_id)
