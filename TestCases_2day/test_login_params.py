import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


from PageObject.LoginPage import loginpage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import Readconfig
from selenium.webdriver.support.wait import WebDriverWait


class Test_Login_Params:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_login_params_004(self,setup,getDataforlogin):
        self.driver = setup
        self.log.info("test_login_params_004 is Started.")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        time.sleep(5)
        self.log.info("go to this Url--->"+self.Url)
        self.lp = loginpage(self.driver)
        self.log.info("login Page Open")
        time.sleep(5)
        self.lp.Enter_UserName(getDataforlogin[0])
        self.log.info("Entering UserName-->"+getDataforlogin[0])
        time.sleep(3)
        self.lp.Enter_Passwaord(getDataforlogin[1])
        self.log.info("Entering Password-->"+getDataforlogin[1])
        self.lp.Click_login()
        self.log.info("Clicking_On_Login_Button")

        if self.lp.Login_Status() == True:
            if getDataforlogin[2]== "pass":
                self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_login_params_004_passed.PNG")
                self.log.info("test_login_params_004 TestCase is pass")
                self.log.info("Clicking on Menu_Button")
                self.lp.Click_menu()
                self.log.info("Clicking on Logout Button")
                self.lp.Click_logout()
                assert True
            else:
                self.driver.save_screenshot(
                    "D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_login_params_004_failed.PNG")

                self.log.info("test_login_002 TestCase is fail")
                assert False

        else:
            if getDataforlogin[2] == "fail":
                assert True

            else:
                assert False

        self.driver.close()
        # yield
        # self.driver.quit()
        self.log.info("<-------Test_login_Params_004 is completed Successfully----->")




