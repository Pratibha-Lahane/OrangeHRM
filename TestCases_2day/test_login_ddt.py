import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


from PageObject.LoginPage import loginpage
from Utilities import XLutilis
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import Readconfig
from selenium.webdriver.support.wait import WebDriverWait


class Test_Login_DDT:

    Url = Readconfig.geturl()
    #username = Readconfig.getusername()
    #password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\TestCases_2day\\TestData\\Login_Data.xlsx"


    def test_Page_Title_ddt_008(self,setup):
        self.driver = setup

        self.log.info("test_Page_Title_ddt_008 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url---->"+self.Url)

        if self.driver.title=="OrangeHRM":
            assert True
            self.log.info("test_Page_Title_ddt_008 is Pass")
            self.log.info("Page Title is --->"+self.driver.title)
        else:
            self.log.info("test_Page_Title_ddt_008 is failed.")
            assert False


        self.driver.close()
        self.log.info("<----------test_Page_Title_ddt_008 is Completed Successfully------>")

    def test_login_ddt_009(self,setup):
        self.driver = setup
        self.log.info("test_login_ddt_009 is Started.")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("go to this Url--->"+self.Url)

        self.lp = loginpage(self.driver)
        self.log.info("login Page Open")
        self.rows = XLutilis.getrowCount(self.path, "Sheet1")
        print("Number Of rows are--->>", self.rows)

        LoginStatus_list = []
        for r in range(2, self.rows+1):
            self.username = XLutilis.readData(self.path, "Sheet1", r, 2)
            self.password = XLutilis.readData(self.path, "Sheet1", r, 3)
            time.sleep(3)
            self.lp.Enter_UserName(self.username)
            self.log.info("Entering UserName-->"+self.username)
            self.lp.Enter_Passwaord(self.password)
            self.log.info("Entering Password-->"+self.password)
            self.lp.Click_login()
            self.log.info("Clicking_On_Login_Button")
            time.sleep(5)

            if self.lp.Login_Status() == True:
                self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\"+self.username+self.password+"_test_login_ddt_009_passed.PNG")
                self.log.info("Clicking on Menu_Button")
                self.lp.Click_menu()
                self.log.info("Clicking on Logout Button")
                self.lp.Click_logout()
                LoginStatus_list.append("Paas")
                XLutilis.WriteData(self.path,"Sheet1", r, 4, "Pass")
            else:
                LoginStatus_list.append("Fail")
                XLutilis.WriteData(self.path,"Sheet1", r, 4, "Fail")
                self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\"+self.username+self.password+"_test_login_ddt_009_failed.PNG")
        print(LoginStatus_list)
        if "Fail" not in LoginStatus_list:
            self.log.info("test_login_ddt_009 TestCase is Fail")
            assert False
        else:
            self.log.info("test_login_ddt_009 TestCase is Pass")
            assert True

        self.driver.close()
        self.log.info("<-------test_login_ddt_009 is completed Successfully----->")









