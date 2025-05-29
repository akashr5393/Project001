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







# ---------------Book Appointment with Default Values-------------
    @pytest.mark.sanity
    @pytest.mark.regression

    def test_Login_04(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.LN =LoginPage(self.driver)
        self.LN.setmake_appointment()
        self.LN.setusername("John Doe")
        self.LN.setpassword("ThisIsNotAPassword")
        self.LN.setlogin()
        time.sleep(2)
        self.LN.setclkfacility()
        self.LN.setfacility("Hongkong CURA Healthcare Center")
        self.LN.sethealthcare("Medicare")
        self.LN.setvisit_date("20225-06-28")
        self.LN.setcomments("This is a test comment")
        self.LN.setclickbook()
        time.sleep(2)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        if "Appointment Confirmation" in body_text:
            print("user successfully book the appointment")
            assert True
        else:
            print("user failed to book the appointment")
            self.driver.save_screenshot(".\\screenshoot\\" and "test_Login_04.png")
            assert False

#















