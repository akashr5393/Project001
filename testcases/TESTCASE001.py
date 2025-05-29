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





    # --------------Verify Homepage Loads Successfully-----------
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homepage_01(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        body_text = self.driver.find_element(By.TAG_NAME,"body").text
        if "Make Appointment" in body_text:
            print("Home page is loads correctly")
        else:
            self.driver.save_screenshot(".\\screenshoot\\" + "test_homepage_01.png")
            print("home page is not loads correctly")



















