import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class addCustomer:
    linkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(), 'Customers')]"
    linkCustomers_menuItem_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a"
    btnAddNew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = '//input[@id="Email"]'
    txtPassword_xpath = '//input[@id="Password"]'
    txtFirstName_xpath = '//input[@id="FirstName"]'
    txtLastName_xpath = '//input[@id="LastName"]'
    radioMaleGender_id = 'Gender_Male'
    radioFemaleGender_id = 'Gender_Female'
    txtDateOfBirthday_xpath = '//input[@id="DateOfBirth"]'
    txtCompanyName_xpath = '//input[@id="Company"]'
    txtAdminComment_xpath = '//textarea[@id="AdminComment"]'
    txtCustomerRoles_xpath = '//*[@id="customer-info"]/div[2]/div[1]/div[10]/div[2]/div/div[1]/div/input'
    lsTitleAdministrators_xpath = '//li[contains(text(), "Administrators")]'
    lsTitleRegistered_xpath = '//li[contains(text(), "Registered")]'
    lsTitleGuests_xpath = '//li[contains(text(), "Guests")]'
    lsTitleVendors_xpath = '//li[contains(text(), "Vendors")]'
    dropManageOfVendor_xpath = '//select[@id="VendorId"]'
    btnSave_xpaht = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menuItem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(1)
        if role == 'Registered':
            self.listItem = self.driver.find_element_by_xpath(self.lsTitleRegistered_xpath)
        elif role == 'Administrators':
            self.listItem = self.driver.find_element_by_xpath(self.lsTitleAdministrators_xpath)
        elif role == 'Guests':
            # here user can be Registered (or) Guest, only one
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listItem = self.driver.find_element_by_xpath(self.lsTitleGuests_xpath)
        elif role == 'Registered':
            self.listItem = self.find_element_by_xpath(self.lsTitleRegistered_xpath)
        elif role == 'verdors':
            self.listItem = self.find_element_by_xpath(self.lsTitleVendors_xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self.listItemGuests_xpath)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).send_keys(role)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).send_keys(Keys.ENTER)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.dropManageOfVendor_xpath))
        time.sleep(3)
        drp.select_by_visible_text(value)
        time.sleep(3)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.radioMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.radioFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.radioMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDateOfBirthday_xpath).send_keys(dob)

    def setCompanyName(self, cname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(cname)

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpaht).click()










