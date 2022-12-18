from selenium.webdriver.common.by import By


class Login:
    txtbx_username_xpath = "//input[@placeholder='Username']"
    txtbx_password_xpath = "//input[@placeholder='Password']"
    btn_login_button ="//button[normalize-space()='Login']"
    txt_pim_xpath = "//span[text()='PIM']"
    mes_invalid_xpath = "//p[text()='Invalid credentials']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.txtbx_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtbx_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_button).click()

    def pim(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_pim_xpath).text
        except:
            None

    def conformationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.mes_invalid_xpath).text
        except:
            None
