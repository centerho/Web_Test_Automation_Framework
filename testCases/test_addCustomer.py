import pytest
import time, string, random
from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import addCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("**************** Test_003_AddCustomer ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** login success ****************")

        self.logger.info("**************** starting add customer Test ****************")

        self.addCust = addCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddnew()

        self.logger.info("**************** Providing customer info ****************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("JH")
        self.addCust.setLastName("Han")
        self.addCust.setDob("7/31/1978")  # Format : D/MM/YYYY
        self.addCust.setCompanyName("SKT")
        self.addCust.setAdminComment("Automated Testing Step")
        self.addCust.clickOnSave()

        self.logger.info("**************** Saving Customer Info ****************")

        self.logger.info("**************** Add Customer validation Started ****************")
        time.sleep(3)
        self.msg = self.driver.find_element_by_tag_name("body").text

        # print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("**************** Add Customer test Passed ****************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" +"test_addCustomer_scr.png")
            self.logger.error("**************** Add Customer test Failed ****************")
            assert True == False
        time.sleep(3)
        self.driver.close()
        self.logger.info("**************** Ending Test_003_AddCustomer ****************")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))