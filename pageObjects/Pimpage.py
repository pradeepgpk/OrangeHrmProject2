import time
from selenium.webdriver.common.by import By


class AddNewEmployee:
    pim_add_xpath = "//button[normalize-space()='Add']"
    fst_name_xpath = "//input[@placeholder='First Name']"
    lst_name_xpath = "//input[@placeholder='Last Name']"
    save_btn_xpath = "//button[normalize-space()='Save']"
    txt_nickname_xpath = "//div[1]/div/div/div/div[2]/input[@class='oxd-input oxd-input--active']"
    other_id_Xpath = "//div[2]/div[1]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    driver_lic_num_xpath = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    lic_exp_date_xpath = "//form/div[2]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    ssn_num_xpath = "//div[3]/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    sin_num_xpath = "//div[3]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    drp_nationality_xpath = "//div[@class='oxd-form-row']/div[1]/div[1]//div[@clear]"
    select_country_xpath = "//*[contains(text(),'Indian')]"
    drp_marital_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_status_xpath = "//*[contains(text(),'Single')]"
    select_married_xpath = "//*[contains(text(),'Married')]"
    dob_xpath = "//form/div[3]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    radio_btn_xpath = "//label[normalize-space()='Male']"
    txt_militaryservice_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    drp_blood_xpath = "//form/div[1]//div[2]//div[@class='oxd-select-text-input']"
    select_type_xpath = "//*[contains(text(),'A+')]"
    pd_save_btn_xpath = "//div[5]/button[@type='submit']"
    pd1_save_btn_xpath = "//div[2]/button"
    txt_employename_xpath = "//div[1]/div/div[2]/div/div/input[@placeholder='Type for hints...']"
    drp_employeename_xpath = "//*[contains(text(),'pradeep')]"
    btn_search_xpath = "//button[@type='submit']"
    btn_edit_xpath = "//button/i[@class ='oxd-icon bi-pencil-fill']"
    btn_delete_xpath = "//button/i[@class='oxd-icon bi-trash']"
    btn_conformdelete_xpath = "//div[3]/button[2]"
    txt_save_mes_xpath = "//*[text()='Successfully Saved']"
    txt_update_mes_xpath = "//*[text()='Successfully Updated']"
    txt_delete_mes_xpath = "//*[text()='Successfully Deleted']"
    def __init__(self, driver):
        self.driver = driver
    def addPim(self):
        self.driver.find_element(By.XPATH,self.pim_add_xpath).click()
    def firstName(self,firstname):
        self.driver.find_element(By.XPATH,self.fst_name_xpath).send_keys(firstname)
    def lastName(self,lastname):
        self.driver.find_element(By.XPATH,self.lst_name_xpath).send_keys(lastname)
    def clickSave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.save_btn_xpath).click()
    def nickName(self,nickname):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.txt_nickname_xpath).send_keys(nickname)
    def otherId(self,otherid):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.other_id_Xpath).send_keys(otherid)
    def drivingLicenseNumber(self,driverlicnum):
        self.driver.find_element(By.XPATH, self.driver_lic_num_xpath).send_keys(driverlicnum)
    def licenseExpiryDate(self,licexpdate):
        self.driver.find_element(By.XPATH, self.lic_exp_date_xpath).send_keys(licexpdate)
    def ssnNumber(self,ssn):
        self.driver.find_element(By.XPATH,self.ssn_num_xpath).send_keys(ssn)
    def sinNumber(self,sin):
        self.driver.find_element(By.XPATH,self.sin_num_xpath).send_keys(sin)
    def nationality(self):
        self.driver.find_element(By.XPATH, self.drp_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.select_country_xpath).click()
    def maritalStatus(self):
        self.driver.find_element(By.XPATH, self.drp_marital_xpath).click()
        self.driver.find_element(By.XPATH, self.select_status_xpath).click()
    def dob(self,dob):
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)
    def gender(self):
        self.driver.find_element(By.XPATH, self.radio_btn_xpath).click()
    def militaryService(self,military_Service):
        self.driver.find_element(By.XPATH, self.txt_militaryservice_xpath).send_keys(military_Service)
    def personalDetailSave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pd_save_btn_xpath).click()
    def bloodType(self):
        self.driver.find_element(By.XPATH, self.drp_blood_xpath).click()
        self.driver.find_element(By.XPATH, self.select_type_xpath).click()
    def customFieldsSave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pd1_save_btn_xpath).click()
    def employeename(self,employeename):
        self.driver.find_element(By.XPATH, self.txt_employename_xpath).send_keys(employeename)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drp_employeename_xpath).click()
    def search(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()
    def edit(self):
        self.driver.find_element(By.XPATH, self.btn_edit_xpath).click()
    def editMaritalStatus(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drp_marital_xpath).click()
        self.driver.find_element(By.XPATH, self.select_married_xpath).click()
        self.driver.find_element(By.XPATH, self.pd_save_btn_xpath).click()
    def delete(self):
        self.driver.find_element(By.XPATH, self.btn_delete_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_conformdelete_xpath).click()
    def saveConformation(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_save_mes_xpath).is_displayed()
        except:
            return False
    def updateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_update_mes_xpath).is_displayed()
        except:
            return False
    def deleteConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_delete_mes_xpath).is_displayed()
        except:
            return False
