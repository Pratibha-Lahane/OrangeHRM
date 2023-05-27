import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObject.AddEmployeePage import AddEmployee
from PageObject.LoginPage import loginpage
from Utilities.ReadProperties import Readconfig
from Utilities.Logger import LogGenerator
from Utilities import XLutilis
#ddt for data driven test
class Test_AddEmp_Ddt:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\TestCases_2day\\TestData\\EmployeeList.xlsx"


    def test_addemp_ddt_007(self,setup):
        self.driver = setup
        self.log.info("test_addemp_ddt_007 Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to this Url---->"+self.Url)
        self.lp = loginpage(self.driver)
        self.log.info("login page open")
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username-->"+self.username)
        self.lp.Enter_Passwaord(self.password)
        self.log.info("Entering password-->"+self.password)
        self.lp.Click_login()
        self.log.info("Click on login Button")
        self.ae = AddEmployee(self.driver)


        self.rows = XLutilis.getrowCount(self.path,"Sheet1")
        print("Number Of rows are--->>", self.rows)

        self.ae.Click_PIM_Menu_Button()
        self.log.info("Click on PIM_Menu Button")

        self.ae.Click_Add_Button()
        self.log.info("Click on Add_Button")

        Status_list = []
        for r in range(2,self.rows+1):
            self.FirstName = XLutilis.readData(self.path, "Sheet1", r, 2)
            self.MiddleName = XLutilis.readData(self.path, "Sheet1", r, 3)
            self.LastName = XLutilis.readData(self.path, "Sheet1", r, 4)
            time.sleep(3)
            self.ae.Enter_FirstName(self.FirstName)
            self.log.info("Entering Firstname-->"+self.FirstName)
            self.ae.Enter_MiddleName(self.MiddleName)
            self.log.info("Entering Middlename-->"+self.MiddleName)
            self.ae.Enter_LastName(self.LastName)
            self.log.info("Entering Lastname-->"+self.LastName)
            time.sleep(3)
            self.ae.Click_save_Button()
            self.log.info("Click on save_Button")
            time.sleep(10)
            if  self.ae.AddEmployee_Status() == True:
                self.ae.Click_Add_Emp_Button()
                self.log.info("click on Add_Emp_Button")
                time.sleep(5)
                Status_list.append("Pass")
                XLutilis.WriteData(self.path,"Sheet1", r ,5 , "Pass")
                self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_addemp_ddt_007_Passed.PNG")
            else:
                Status_list.append("Fail")
                XLutilis.WriteData(self.path,"Sheet1", r ,5 , "Fail")

                self.driver.save_screenshot("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\ScreenShoots\\test_addemp_003_Failed.PNG")
        print(Status_list)
        time.sleep(2)
        self.lp.Click_menu()
        self.log.info("Clicking on Menu_Button")
        time.sleep(2)
        self.lp.Click_logout()
        self.log.info("Clicking on Logout Button")
        time.sleep(2)
        self.driver.close()
        if "Fail" not in Status_list:
            self.log.info("test_addemp_ddt_007 Testcase is Passed.")

            assert True
        else:
            self.log.info("test_addemp_ddt_007 Testcase is Failed.")

            assert False

        self.log.info("<-------test_addemp_ddt_007 Testcase is Completed Successfully------>")



