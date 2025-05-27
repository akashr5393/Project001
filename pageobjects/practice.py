from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select



class orangeAT:
   username_xpath = "//input[@placeholder='auth.username']"
   password_xpath = "//input[@placeholder='Password']"
   login_xpath = "//button[normalize-space()='Login']"
   admin_xpath = "//a[normalize-space()='']"
   addnew_xpath = "//button[normalize-space()='Add']"
   userroll_class = "oxd-select-text-input"
   employeename_xpath = "//input[@placeholder='Type for hints...']"
   satus_xpath = "//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-select-text-input']"
   USERNAME_XPATH = "//input[@class='oxd-input oxd-input--active']"
   PASSWORD_XPATH = "(//input[@type='password'])[1]"
   CONFORMPASSWORD_XPATH = "(//input[@type='password'])[2]"
   SAVE_XPATH = "//button[normalize-space()='Save']"



   def __init__(self,driver):
       self.driver = driver

   def setusername(self,username):
       self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

   def setpassword(self,password):
       self.driver.find_element(By.XPATH,self.PASSWORD_XPATH).send_keys(password)

   def setclicklogin(self):
       self.driver.find_element(By.XPATH,self.login_xpath).click()

   def setadmin(self):
       self.driver.find_element(By.XPATH,self.admin_xpath).click()


   def setaddnew(self):
        self.driver.find_element(By.XPATH,self.addnew_xpath).click()

   def setuserroll(self,userroll):
       select = Select(self.driver.find_element(By.XPATH,self.userroll_class))
       select.select_by_visible_text(userroll)

   def setemployeename(self,employeename):
       self.driver.find_element(By.XPATH,self.employeename_xpath).send_keys(employeename)

   def setstatus(self,status):
      select = Select( self.driver.find_element(By.XPATH,self.satus_xpath))
      select.select_by_visible_text(status)

   def setUSERNAME(self,USERNAME):
       self.driver.find_element(By.XPATH,self.username_xpath).send_keys(USERNAME)

   def setPASSWORD(self,PASSWORD):
       self.driver.find_element(By.XPATH,self.PASSWORD_XPATH).send_keys(PASSWORD)


   def setCONFORMPASSWORD(self,CONFORMPASSWORD):
       self.driver.find_element(By.XPATH,self.CONFORMPASSWORD_XPATH).send_keys(CONFORMPASSWORD)

   def setSAVE(self):
       self.driver.find_element(By.XPATH,self.SAVE_XPATH).click()



