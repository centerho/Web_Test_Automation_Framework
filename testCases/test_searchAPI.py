import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.searchAPIPage import searchAPI
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_SearchAPI:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchAPI(self,setup):
        self.logger.info("********** Test_004_SearchAPI **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** login success **********")
        self.logger.info("********** starting Search API **********")

        self.srcAPI = searchAPI(self.driver)
        time.sleep(1)
        self.srcAPI.clickOnAPIMenu()
        time.sleep(1)

        self.logger.info("********** searching API **********")
        # 검색을 위해서 임의의 값 value를 넣어줌
        value = "11번가"
        self.srcAPI.setAPI(value)
        time.sleep(1)
        self.srcAPI.clickSearch()
        time.sleep(3)

        self.logger.info("********** Search API validation Started **********")
        # 프로젝트 생성 검증을 위해 body에서 text값만 msg에 넣어줌
        self.msg = self.driver.find_element_by_tag_name("body").text

        if value in self.msg:
            assert True == True
            self.logger.info("********** Search API test Passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" +"test_searchAPI_scr.png")
            self.logger.error("********** Search API test Failed **********")
            assert True == False
        time.sleep(2)

        self.driver.close()
        self.logger.info("********** Ending Test_004_Search API **********")


