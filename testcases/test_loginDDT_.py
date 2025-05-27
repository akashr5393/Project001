
import time
import pytest
from pageobjects.loginpage import LoginPage
from utilities.readprapaties import ReadConfig
from utilities.costmlogger import LogGen
from utilities import XLUNITS

class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplication()
    path = ".//TestData/Cleaned_Interest_Calculation_Example.xlsx"
    logger = LogGen.loggen()

    def test_Login_DDT(self, setup):
        self.logger.info("********* Starting DDT Login Test *********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)  # FIXED: Create page object

        lst_status = []
        rows = XLUNITS.getRowCount(self.path, "Sheet1")
        print("Number of rows in Excel:", rows)

        for r in range(2, rows + 1):
            username = XLUNITS.readData(self.path, "Sheet1", r, 1)
            password = XLUNITS.readData(self.path, "Sheet1", r, 2)
            expected_result = XLUNITS.readData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(username)
            self.lp.setPassword(password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Swag Labs"

            if act_title == exp_title:
                if expected_result.lower() == "pass":
                    self.logger.info(f"[Row {r}] Login successful as expected.")
                    lst_status.append("pass")
                else:
                    self.logger.info(f"[Row {r}] Login successful but expected fail.")
                    lst_status.append("fail")
                # self.lp.clickout() # Add logout if needed
                self.driver.get(self.baseurl)  # Go back to login page
            else:
                if expected_result.lower() == "fail":
                    self.logger.info(f"[Row {r}] Login failed as expected.")
                    lst_status.append("pass")
                else:
                    self.logger.info(f"[Row {r}] Login failed but expected pass.")
                    lst_status.append("fail")

        # Final validation
        if "fail" not in lst_status:
            self.logger.info("**** DDT Login Test PASSED ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** DDT Login Test FAILED ****")
            self.driver.close()
            screenshot_path = ".\\screenshot\\test_Login_DDT.png"
            assert False
