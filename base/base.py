import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time


class Base:

    def __init__(self, driver):
        self.driver = driver

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        input_valuse = self.search_ele(loc, timeout, poll_frequency)
        input_valuse.clear()
        input_valuse.send_keys(text)

    def swipe_screen(self, tag=1):

        # 获取分辨率
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        time.sleep(2)

        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8)

        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5)
        if tag == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5)

    def get_toast(self, ts):

        # xpath
        message_xpath = (By.XPATH, "//*[contains(@text,'{}')]".format(ts))
        return self.search_ele(message_xpath, timeout=3, poll_frequency=0.3).text

    def screen_png(self, name="截图"):
        # 图片名称
        png_name = "{}.png".format(int(time.time()))
        # 截图
        self.driver.get_screenshot_as_file("./image" + os.sep + png_name)

        with open("./image" + os.sep + png_name, "wb") as f:
            allure.attach(name, f.read(), allure.attach_type.PNG)
