
import pytest
from selenium import webdriver
from pageobjects.loginpage import LoginPage
from utilities.readprapaties import ReadConfig
from utilities.costmlogger import LogGen
import os


class Test_001_Login:
    baseurl = ReadConfig.getApplication()
    username = ReadConfig.getusername()
    admin_password = ReadConfig.getadminpassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_homepageTitle(self, setup):
        self.logger.info("********************* Test_001_Login: test_homepageTitle **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info(f"Navigated to {self.baseurl}")

        actual_title = self.driver.title
        expected_title = "Swag Labs"

        if actual_title == expected_title:
            self.logger.info("Homepage title matched. Test passed.")
            assert True
        else:
            screenshot_path = ".\\screenshot\\test_homepageTitle.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Homepage title mismatch. Actual title: {actual_title}. Screenshot saved.")
            assert False
        self.driver.close()

    # @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("********************* Test_001_Login: test_Login **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info(f"Navigated to {self.baseurl}")

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.admin_password)
        self.lp.clickLogin()
        # assert "Swag Labs" in self.driver.title, "Login failed or incorrect page title"

        self.logger.info("login successful")
        # self.lp.clickaddcart()
        # self.lp.shoppingCart()
        # self.lp.clickRemove()

        # car_item = self.driver.find_element(By.CLASS_NAME,"cart_item")
        # assert  len(car_item) == 0,"item not removed from cart"

        actual_title = self.driver.title
        expected_title = "Swag Labs"

        if actual_title == expected_title:
            self.logger.info("Login successful. Test passed.")
            assert True
        else:
            screenshot_path = ".\\screenshot\\test_Login.png"
            # os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Login failed. Screenshot saved.")
            assert False
        self.driver.close()





