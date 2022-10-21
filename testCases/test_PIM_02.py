import time

from pageObjects.LoginPage import Login
from pageObjects.Pimpage import AddNewEmployee
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_PIM_02:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def test_edit_employee(self, setup):
        self.logger.info("***************** TC_PIM_02 ****************************")
        self.logger.info("***************** Varifying Edit an exiting employee ****************************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUserName(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()
        self.logger.info("***************** Successfully Login ****************************")
        self.pimpageobj = AddNewEmployee(self.driver)
        self.pimpageobj.employeename("pradeep")
        self.pimpageobj.search()
        self.pimpageobj.edit()
        self.pimpageobj.editMaritalStatus()
        self.update = self.pimpageobj.updateConformation()
        time.sleep(3)
        if self.update == True:
            self.logger.info("***************** Successfully Edit an exiting employee *******************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************** Edit an exiting employee Unsuccessful  ******************")
            self.driver.close()
            assert False
        self.logger.info("************** Completed TC_PIM_02 *********************")


