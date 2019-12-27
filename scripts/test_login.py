import pytest ,sys ,os
sys.path.append(os.getcwd())
from base.page import Page
from base.getDriver import get_android_driver
from base.getData import GetData
import allure

def login_value():
    lis = []
    data = GetData().get_yml_data("login.yml")
    for i in data.values():
        lis.append(tuple(i.values()))
    return lis


class TestLogin:

    def setup_class(self):
        self.driver = get_android_driver("com.bjcsxq.chat.carfriend", ".module_main.activity.MainActivity")
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_person(self):
        self.page_obj.get_home_page().click_after_btn()
        self.page_obj.get_home_page().click_my_btn()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        self.page_obj.get_person_page().click_login_sigin_btn()

    @pytest.mark.parametrize("phone,passwd,mess,expData", login_value())
    def test_login(self, phone, passwd, mess, expData):
        # 登录
        self.page_obj.get_login_page().login(phone, passwd)
        # 判断
        if mess:

            toast_message = self.page_obj.get_person_page().get_toast(mess)
            try:
                assert toast_message == expData
            except AssertionError:
                # 截图
                self.page_obj.get_setting_page().screen_png("预期断言失败截图")

                # 抛异常
                raise
            finally:
                self.page_obj.get_login_page().click_return_btn()
        else:

            self.page_obj.get_login_page().click_login_acc_btn()
            username = self.page_obj.get_person_page().get_username()
            try:
                assert username == expData
            except AssertionError:
                # 截图
                self.page_obj.get_setting_page().screen_png("预期断言成功截图")
                # 抛异常
                raise
            finally:
                self.page_obj.get_person_page().click_setting_btn()
                self.page_obj.get_setting_page().logout()
