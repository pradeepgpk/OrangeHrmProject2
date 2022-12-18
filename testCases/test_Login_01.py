import time
from pageObjects.LoginPage import Login
from utilities import customlogger
from utilities.readproperties import ReadConfig

class Test_Login_01:

    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def test_login(self, setup):
        self.logger.info("***************** TC_Login_01 ***********************")
        self.logger.info("***************** Varifying Employee Login ***********************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUserName(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()
        self.confmsg = self.loginpageobj.pim()
        time.sleep(3)
        if self.confmsg == "PIM":
            self.logger.info("***************** Login Successful Test Is Passed ***********************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "TC_login_01.png")
            self.logger.info("***************** Login Unsuccessful Test Is Failed ***********************")
            # self.driver.close()
            assert False
        self.logger.info("************** Completed TC_Login_01 *********************")
