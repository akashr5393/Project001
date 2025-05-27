from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select



class BANK:
    register_xpath = "//a[normalize-space()='Register']"
    firstname_xpath = "//input[@id='customer.firstName']"
    lastname_xpath = "//input[@id='customer.lastName']"
    address_xpath = "//input[@id='customer.address.street']"
    city_xpath = "//input[@id='customer.address.city']"
    state_xpath = "//input[@id='customer.address.state']"
    zipcode_xpath = "//input[@id='customer.address.zipCode']"
    phoneno_xpath = "//input[@id='customer.phoneNumber']"
    snn_xpath = "//input[@id='customer.ssn']"
    username_xpath = "//input[@id='customer.username']"
    password_xpath = "//input[@id='customer.password']"
    confirm_xpath = "//input[@id='repeatedPassword']"
    click_register_xpath = "//input[@value='Register']"

    # user login---------------
    userlogin_xpath = "input"
    userpassworld_xpath = "//input[@name='password']"
    userclicklogin_xpath = "//input[@value='Log In']"
    opennew_account_xpath = "//a[normalize-space()='Open New Account']"
    acco_type = "type"
    # fromaccount_xpath = "//select[@id='fromAccountId']"
    clickopennewaccount_xpath = "//input[@value='Open New Account']"




    def __init__(self,driver):
        self.driver = driver

    def setregister(self):
        self.driver.find_element(By.XPATH,self.register_xpath).click()

    def setfirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.firstname_xpath).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element(By.XPATH,self.lastname_xpath).send_keys(lastname)

    def setaddress(self,address):
        self.driver.find_element(By.XPATH,self.address_xpath).send_keys(address)

    def setcity(self,city):
        self.driver.find_element(By.XPATH,self.city_xpath).send_keys(city)

    def setstate(self,state):
        self.driver.find_element(By.XPATH,self.state_xpath).send_keys(state)

    def setzipcode(self,zipcode):
        self.driver.find_element(By.XPATH,self.zipcode_xpath).send_keys(zipcode)

    def setphone(self,phone):
        self.driver.find_element(By.XPATH,self.phoneno_xpath).send_keys(phone)

    def setssn(self,ssn):
        self.driver.find_element(By.XPATH,self.snn_xpath).send_keys(ssn)

    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def setconfirm(self,confirm):
        self.driver.find_element(By.XPATH,self.confirm_xpath).send_keys(confirm)

    def setclickregister(self):
        self.driver.find_element(By.XPATH,self.click_register_xpath).click()

    #     user login-----------

    def setuserlogin(self,userlogin):
        self.driver.find_element(By.CLASS_NAME,self.userlogin_xpath).send_keys(userlogin)

    def setuserpassword(self,userpassword):
        self.driver.find_element(By.XPATH,self.userpassworld_xpath).send_keys(userpassword)

    def setuserclicklogin(self):
        self.driver.find_element(By.XPATH,self.userclicklogin_xpath).click()
    def setnewaccount(self):
        self.driver.find_element(By.XPATH,self.opennew_account_xpath).click()

    def setacctype(self,accctype):
       self.driver.find_element(By.ID,self.acco_type)


    def setopennewaccount(self):
        self.driver.find_element(By.XPATH,self.opennew_account_xpath).click()





