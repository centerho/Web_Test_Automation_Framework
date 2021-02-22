import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()   # URL정보를 가져옴
    path = '.\\testData\\LoginData.xlsx'       # Test Data 파일 경로
    logger = LogGen.loggen()                   # 로그 생성을 위한 인스턴스

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** verifying login DDT test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        # Test data 의 행 숫자를 가져옴
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        # PASS/FAIL 정보를 넣어줄 빈 리스트 생성
        lst_status = []

        for r in range(2, self.rows+1):
            # Test data에서 엑셀 셀값을 가져옴
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            self.driver.get(self.baseURL)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "SK open API"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("********** Failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Failed")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("********** Passed")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********** Login DDT Test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDT Test Failed **********")
            self.driver.close()
            assert False

        self.logger.info("********** End of Login DDT Test **********")
        self.logger.info("********** Completed TC_LoginDDT_002 **********")