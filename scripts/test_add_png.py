import allure, os


class TestAddPng():

    def test_001(self):
        with open("./image"+os.sep+"mao.png","rb") as f:
            allure.attach("mao",f.read(),allure.attach_type.PNG)
        assert True