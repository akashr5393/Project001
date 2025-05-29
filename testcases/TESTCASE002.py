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







    # -------------- Verify Login with Valid Credentials--------------
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_02(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.LN =LoginPage(self.driver)
        self.LN.setmake_appointment()
        self.LN.setusername("John Doe")
        self.LN.setpassword("ThisIsNotAPassword")
        self.LN.setlogin()
        act_title = self.driver.title
        print(act_title)
        body_text = self.driver.find_element(By.TAG_NAME,"body").text
        if act_title in body_text:
            print("user successfully Redirected to the appointment form page")
            assert True
        else:
            print("user failed to redirect to the appointment form page")
            self.driver.save_screenshot(".\\screenshoot\\" + "test_Login_02.png")

            assert False


















