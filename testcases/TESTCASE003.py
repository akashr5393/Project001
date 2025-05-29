import time

import pytest
from selenium import webdriver
from pageobjects.project001 import LoginPage
from utilities.readprapaties import ReadConfig
from utilities.costmlogger import LogGen
from selenium.webdriver.common.by import By

import os


class Test_001_Login:
    baseurl = "https://katalon-demo-cura.herokuapp.com/"







# --------------Verify Login with Invalid Credentials-------------
    @pytest.mark.regression
    def test_Login_03(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.LN =LoginPage(self.driver)
        self.LN.setmake_appointment()
        self.LN.setusername("John D")
        self.LN.setpassword("ThisIsNotAPassword")
        self.LN.setlogin()
        act_title = self.driver.title
        print(act_title)
        body_text = self.driver.find_element(By.TAG_NAME,"body").text
        if "Login failed! Please ensure the username and password are valid." in body_text:
            print("system successfully show Login error message displayed")
            assert True
        else:
            print("system does not  show Login error message displayed and user logged in")
            self.driver.save_screenshot(".\\screenshoot\\" + "test_Login_03.png")
            assert False


















