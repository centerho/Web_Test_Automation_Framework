class LoginPage:
    # Element를 찾기 위한 변수와 속성 지정
    textbox_username_id = "loginId"
    textbox_password_id = "loginPassword"
    button_login_xpath = "//*[@id='btnLogin']"
    link_logout_linktext = "로그아웃"

    def __init__(self, driver):
        self.driver = driver

    # ID 입력란을 Clear 한 후 username 입력
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    # Password 입력란을 Clear 한 후 password 입력
    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    # 로그인 버튼 클릭
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    # 로그아웃 버튼 클릭
    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
