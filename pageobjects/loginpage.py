

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_id = "user-name"
        self.textbox_password_id = "password"
        self.button_login_xpath = "//input[@id='login-button']"
        # self.add_cart_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
        # self.shopping_cart_xpath = "//span[@class='shopping_cart_badge']"
        # self.remove_xpath = "//button[@id='remove-sauce-labs-backpack']"


    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


    # def clickaddcart(self):
    #     self.driver.find_element(By.XPATH,self.add_cart_xpath).click()
    #
    # def shoppingCart(self):
    #     self.driver.find_element(By.XPATH,self.shopping_cart_xpath).click()
    #
    # # In LoginPage class:
    # def clickRemove(self):
    #     self.driver.find_element(By.XPATH, self.remove_xpath).click()


    # def clickBurgerMenu(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     self.driver.find_element(By.XPATH, self.burger_menu_xpath).click()
    #
    # def clickLogout(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     self.driver.find_element(By.ID, self.log_out_id).click()
