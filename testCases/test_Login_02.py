import time
from pageObjects.LoginPage import Login
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Login_02:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    logger = customlogger.test_logDemo()

    def test_login(self, setup):
        self.logger.info("***************** TC_Login_02 ***********************")
        self.logger.info("***************** Varifying Invalid Employee login ***********************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUserName(self.username)
        self.loginpageobj.setPassword("Invalid password")
        self.loginpageobj.clickLogin()
        self.confmsg = self.loginpageobj.conformationmsg()
        time.sleep(3)
        if self.confmsg == "Invalid credentials":
            self.logger.info("***************** Login Unsuccessful TestCase passed ***********************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "TC_login_02.png")
            self.logger.info("***************** TestCase Failed ***********************")
            self.driver.close()
            assert False
        self.logger.info("************** Completed TC_Login_02 *********************")
