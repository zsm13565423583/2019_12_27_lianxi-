from page.homePage import HomePage
from page.personPage import PersonPage
from page.loginPage import LoginPage
from page.settingPage import SettingPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)

    def get_person_page(self):
        return PersonPage(self.driver)

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_setting_page(self):
        return SettingPage(self.driver)
