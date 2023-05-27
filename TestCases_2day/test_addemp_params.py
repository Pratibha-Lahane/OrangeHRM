import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObject.AddEmployeePage import AddEmployee
from PageObject.LoginPage import loginpage
from Utilities.ReadProperties import Readconfig
from Utilities.Logger import LogGenerator


class Test_AddEmp_Params:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()


    def test_addemp_params_005(self,setup,getDataforAddemp):
        self.driver = setup
        print("data from getDataforAddemp prams",getDataforAddemp)
        self.log.info("test_addemp_params_005 Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to this Url---->"+self.Url)
        self.ae = AddEmployee(self.driver)
        self.lp = loginpage(self.driver)
        self.log.info("login page open")
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username-->"+self.username)
        self.lp.Enter_Passwaord(self.password)
        self.log.info("Entering password-->"+self.password)
        self.lp.Click_login()
        self.log.info("Click on login Button")

        self.ae.Click_PIM_Menu_Button()
        self.log.info("Click on PIM_Menu Button")

        self.ae.Click_Add_Button()
        self.log.info("Click on Add_Button")

        self.ae.Enter_FirstName(getDataforAddemp[0])
        self.log.info("Entering Firstname-->",getDataforAddemp[0])

        self.ae.Enter_MiddleName(getDataforAddemp[1])
        self.log.info("Entering Middlename-->",getDataforAddemp[1])

        self.ae.Enter_LastName(getDataforAddemp[2])
        self.log.info("Entering Lastname-->",getDataforAddemp[2])

        self.ae.Click_save_Button()
        self.log.info("Click on save_Button")

        if  self.ae.AddEmployee_Status()==True:
            if getDataforAddemp[3] == "pass":
               self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_addemp_params_005_Passed.PNG")
               self.log.info("test_addemp_params_005 Testcase is Passed.")
               self.lp.Click_menu()
               self.log.info("Clicking on Menu_Button")

               self.lp.Click_logout()
               self.log.info("Clicking on Logout Button")
               assert True
            else:
                self.driver.save_screenshot(
                    "D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_addemp_params_005_Failed.PNG")
                self.log.info("test_addemp_params_005 Testcase is Failed.")
                assert False
        else:
            if getDataforAddemp[3] == "fail":
                self.log.info("Invalid Credential But condition Satisfy")
                assert True
            else:
                self.log.info("Invalid Credential But condition Not Satisfy")
                assert False
        self.driver.close()
        self.log.info("<-------test_addemp_params_005 Testcase is Completed Successfully------>")

        




