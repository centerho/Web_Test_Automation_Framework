import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import addCustomer
from pageObjects.searchCustomerPage import searchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("**************** Test_004_SearchCustomerByEmail ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** login success ****************")

        self.logger.info("**************** starting Search Customer By Email ****************")

        self.addCust = addCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.logger.info("**************** searching customer by emailID ****************")
        searchCust = searchCustomer(self.driver)
        searchCust.setEmail("james_pan@nopCommerce.com")
        searchCust.clickSearch()
        time.sleep(3)
        status = searchCust.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True == status
        self.logger.info("**************** Ending Test_004_SearchCustomerByEmail ****************")

        self.driver.close()
