import pytest
# Login Page에서 사용할 메소드 들
from pageObjects.LoginPage import LoginPage
# config 정보를 읽어오는 클래스
from utilities.readProperties import ReadConfig
# Log 정보를 생성해주는 메소드
from utilities.customLogger import LogGen

class Test_001_Login:
    # config 파일에서 URL, ID, PW 정보를 가져옴
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # Log 생성을 위한 인스턴스
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** verifying home page title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        # 현재 탭의 타이틀 정보를 가져옴
        act_title = self.driver.title
        # 타이틀 정보를 이용해서 로그인 페이지가 정상적으로 열렸는지 검증
        if act_title == "로그인 - SK open API":
            assert True
            self.driver.close()
            self.logger.info("********** Login page title test is passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Login page title test is failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** verifying login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # ID, PW 입력
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        # 로긴 버튼 클릭
        self.lp.clickLogin()
        # 로긴 후 타이틀 정보 저장
        act_title = self.driver.title
        if act_title == "SK open API":
            assert True
            self.logger.info("********** login test is passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********** login test is failed **********")
            assert False
