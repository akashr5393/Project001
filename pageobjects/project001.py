import select
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class LoginPage:
    clkmake_appointment = "//a[@id='btn-make-appointment']"
    username_xpath = "//input[@id='txt-username']"
    password_xpath = "//input[@id='txt-password']"
    login_xpath = "//button[@id='btn-login']"

    clik_Facility_xpath = "//select[@id='combo_facility']"
    Facility_xpath = "//select[@id='combo_facility']"
    Medicare_xpath = "//input[@id='radio_program_medicare']"
    Medicaid_xpath = "//input[@id='radio_program_medicare']"
    None_xpath = "//input[@id='radio_program_none']"
    Visit_date_xpath = "//input[@id='txt_visit_date']"
    comment_xpath = "//textarea[@id='txt_comment']"
    clickbook_xpath = "//button[@id='btn-book-appointment']"
    gotohome_xpath = "//a[normalize-space()='Go to Homepage']"
    bars_xpath = "//i[@class='fa fa-bars']"
    history_xpath = "//a[normalize-space()='History']"
    back_xpath = "//a[normalize-space()='Go to Homepage']"




    def __init__(self, driver):
        self.driver = driver

    def setmake_appointment(self):
        self.driver.find_element(By.XPATH,self.clkmake_appointment).click()

    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def setlogin(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def setclkfacility(self):
        self.driver.find_element(By.XPATH, self.Facility_xpath).click()



    def setfacility(self,facility):

        select = Select(self.driver.find_element(By.XPATH,self.Facility_xpath))
        select.select_by_visible_text(facility)

    def sethealthcare(self,healthcare):
        time.sleep(2)
        if healthcare == "Medicare":
            self.driver.find_element(By.XPATH,self.Medicare_xpath).click()
        elif healthcare ==  "Medicare":
            self.driver.find_element(By.XPATH,self.Medicaid_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.None_xpath).click()

    def setvisit_date(self,visit_date):
        self.driver.find_element(By.XPATH,self.Visit_date_xpath).send_keys(visit_date)

    def setcomments(self,comments):
        self.driver.find_element(By.XPATH,self.comment_xpath).send_keys(comments)

    def setclickbook(self):
        self.driver.find_element(By.XPATH,self.clickbook_xpath).click()

    def setgotohome(self):
        self.driver.find_element(By.XPATH,self.gotohome_xpath).click()

    def setbars(self):
        self.driver.find_element(By.XPATH,self.bars_xpath).click()

    def sethistory(self):
        self.driver.find_element(By.XPATH,self.history_xpath).click()

    def setback(self):
        self.driver.find_element(By.XPATH,self.back_xpath).click()














