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







# ---------------- Verify Appointment History Link Verify Appointment History Link----
    @pytest.mark.regression

    def test_Login_05(self,setup):
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
        self.LN.setgotohome()
        self.LN.setbars()
        self.LN.sethistory()
        time.sleep(2)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        if "History" in body_text:
            print("user successfully  Verify Appointment History")
            assert True
        else:
            print("user failed Verify Appointment History")
            self.driver.save_screenshot(".\\screenshoot\\" + "test_Login_05.png")
            assert False
        time.sleep(2)

        self.LN.setback()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        if "We Care About Your Health" in body_text:
            print("user back to the home page")
            assert True
        else:
            print("user failed to back to the home page")
            assert False

















