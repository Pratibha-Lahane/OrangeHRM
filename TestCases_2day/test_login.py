import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


from PageObject.LoginPage import loginpage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import Readconfig
from selenium.webdriver.support.wait import WebDriverWait


class Test_Login:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_Page_Title_001(self,setup):
        self.driver = setup
        #self.log.warning("warning")

        self.log.info("test_Page_Title_001 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url---->"+self.Url)
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        if self.driver.title=="OrangeHRM":
            assert True
            self.log.info("test_page_Title_001 is Pass")
            self.log.info("Page Title is --->"+self.driver.title)
        else:
            self.log.info("test_page_Title_001 is failed.")
            assert False


        self.driver.close()
        self.log.info("<----------test_Page_Title_001 is Completed Successfully------>")

    @pytest.mark.sanity
    def test_login_002(self,setup):
        self.driver = setup
        self.log.info("test_login_002 is Started.")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("go to this Url--->"+self.Url)
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.lp = loginpage(self.driver)
        self.log.info("login Page Open")
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering UserName-->"+self.username)
        self.lp.Enter_Passwaord(self.password)
        self.log.info("Entering Password-->"+self.password)
        self.lp.Click_login()
        self.log.info("Clicking_On_Login_Button")

        if self.lp.Login_Status() == True:
            self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_login_002_passed.PNG")
            self.log.info("test_login_002 TestCase is pass")
            self.log.info("Clicking on Menu_Button")
            self.lp.Click_menu()
            self.log.info("Clicking on Logout Button")
            self.lp.Click_logout()
            assert True
        else:
            self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_login_002_failed.PNG")
            self.log.info("test_login_002 TestCase is fail")

            assert False

        self.driver.close()
        self.log.info("<-------Test_login_002 is completed Successfully----->")
        #######################################################################
        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("Critical")
        #########################################################
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        #
        # try:
        #     self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        #     print("test_login_001 TestCase is pass")
        #
        #     self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     assert True
        # except NoSuchElementException:
        #
        #     print("test_login_001 Testcase is fail")
        #     assert False




