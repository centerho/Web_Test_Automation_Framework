class searchAPI:
    linkAPI_menu_xpath = '//*[@id="gnb"]/li[1]/a'
    txtSearch_id = "srchKeyword"
    btnSearch_xpath = '//*[@id="btnSearch"]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnAPIMenu(self):
        self.driver.find_element_by_xpath(self.linkAPI_menu_xpath).click()

    def setAPI(self, api):
        self.driver.find_element_by_id(self.txtSearch_id).clear()
        self.driver.find_element_by_id(self.txtSearch_id).send_keys(api)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def getPage(self):
        return self.driver.find_element_by_tag_name("body").text




