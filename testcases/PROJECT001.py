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

















