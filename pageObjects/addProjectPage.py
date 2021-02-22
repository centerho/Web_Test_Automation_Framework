import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class addProject:
    linkMyProject_menu_xpath = '//*[@id="gnb"]/li[6]/a'
    btnNewProject_ID = "myprojectCreateVeiw"
    btnConfirm_ID = "myprojectCreate"
    txtProjectName_xpath ='//*[@id="myprojectName"]'
    txtProjectDesc_ID = "myprojectDesc"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMyProjectMenu(self):
        self.driver.find_element_by_xpath(self.linkMyProject_menu_xpath).click()

    def clickOnNewProject(self):
        self.driver.find_element_by_id(self.btnNewProject_ID).click()

    def setProjectName(self, Pname):
        self.driver.find_element_by_xpath(self.txtProjectName_xpath).send_keys(Pname)

    def setProjectDesc(self, Desc):
        self.driver.find_element_by_id(self.txtProjectDesc_ID).send_keys(Desc)

    def clickConfirm(self):
        self.driver.find_element_by_id(self.btnConfirm_ID).click()

    def clickAlert(self):
        Alert(self.driver).accept()











