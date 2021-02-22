import pytest
import time, string, random
from pageObjects.LoginPage import LoginPage
from pageObjects.addProjectPage import addProject
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddProject:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addProject(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** login success **********")

        self.logger.info("********** starting add Project Test **********")
        # 로그인 이후 메뉴>My Project로 이동해서 프로젝트 생성 클릭
        self.addPrj = addProject(self.driver)
        time.sleep(1)
        self.addPrj.clickOnMyProjectMenu()
        time.sleep(1)

        self.addPrj.clickOnNewProject()
        self.logger.info("********** Providing Project info **********")
        time.sleep(1)
        # 프로젝트 이름을 랜덤으로 생성해서 입력
        self.prjName = random_generator()
        self.addPrj.setProjectName(self.prjName)
        # 프로젝트 설명에는 고정값 입력
        self.addPrj.setProjectDesc("This is Test Description.")
        # 프로젝트 생성 창에서 확인 누르기
        self.addPrj.clickConfirm()
        time.sleep(2)
        # 경고창에서 확인 누르기
        self.addPrj.clickAlert()
        self.logger.info("********** Saving Project Info **********")
        time.sleep(2)

        self.logger.info("********** Add Project validation Started **********")
        # 프로젝트 생성 검증을 위해 body에서 text값만 msg에 넣어줌
        self.msg = self.driver.find_element_by_tag_name("body").text
        # msg에 random으로 생성한 prjName이 있는지 확인, 있다면 True, 없으면 False
        if self.prjName in self.msg:
            assert True == True
            self.logger.info("********** Add Project test Passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" +"test_addProject_scr.png")
            self.logger.error("********** Add Project test Failed **********")
            assert True == False
        time.sleep(2)
        self.driver.close()
        self.logger.info("********** Ending Test_003_AddCustomer **********")

# random으로 8자 단어를 생성
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))