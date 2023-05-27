from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec


class loginpage:
    Text_Username_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Text_Passwaord_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[normalize-space()='Login']")
    Click_Menu_Button_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver = driver

    def Enter_UserName(self,username):
        self.driver.find_element(*loginpage.Text_Username_XPATH).send_keys(username)

    def Enter_Passwaord(self, password):
        self.driver.find_element(*loginpage.Text_Passwaord_XPATH).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*loginpage.Click_Login_Button_XPATH).click()

    def Click_menu(self):
        self.driver.find_element(*loginpage.Click_Menu_Button_XPATH).click()

    def Click_logout(self):
        self.driver.find_element(*loginpage.Click_Logout_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
            return True
        except Ec:
            return False




