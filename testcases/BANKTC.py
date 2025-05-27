import time
from tkinter.tix import Select

import pytest
from selenium import webdriver
from pageobjects.BANKAPP import BANK
from selenium.webdriver.common.by import By
import random
import string
from datetime import datetime


import os


class TestBANK:

    url = "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"
    account = "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"
    # username = "Admin"
    # admin_password = "admin123"



    def test_bank_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(10)
        self.BK = BANK(self.driver)
        self.BK.setregister()
        self.BK.setfirstname('akash')
        self.BK.setlastname('r')
        self.BK.setaddress('bm road')
        self.BK.setcity('bengaluru')
        self.BK.setstate('karnataka')
        self.BK.setzipcode("123456")
        self.BK.setphone("123456788")
        self.BK.setssn("efefm")
        self.BK.setusername('akakas0')
        self.BK.setpassword('llllll22ew2ee')
        self.BK.setconfirm("llllll22ew2ee")
        self.BK.setclickregister()

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        print(self.msg)

        if 'Congratulations, your account is now open.' in self.msg:
            print("user successfully logged in")
            assert True
        else:
            print("user failed to log in ")
            assert False

    time.sleep(3)
    def test_create_account(self,setup):
        self.driver = setup
        self.CA = BANK(self.driver)

        self.driver.get(self.url)
        time.sleep(3)

        self.CA.setuserlogin("akakas123457")
        self.CA.setuserpassword("llllll22ew2ee")
        self.CA.setuserclicklogin()
        self.CA.setnewaccount()
        self.CA.setacctype('SAVING')


        self.CA.setopennewaccount()

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        print(self.msg)

        if 'Open New Account' in self.msg:
            print("user successfully create new account")
            assert True
        else:
            print("user failed to create new account ")
            assert False


















