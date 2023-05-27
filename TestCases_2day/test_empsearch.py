import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from PageObject.AddEmployeePage import AddEmployee
from PageObject.EmployeeSearch_Page import EmployeeSearch
from PageObject.LoginPage import loginpage
from Utilities.ReadProperties import Readconfig
from Utilities.Logger import LogGenerator


class Test_SearchEmp:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_searchemp_006(self,setup):
        self.driver = setup
        self.log.info("test_searchemp_006 Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to this Url---->"+self.Url)
        self.ae = AddEmployee(self.driver)
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
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


        self.se = EmployeeSearch(self.driver)
        self.se.Click_on_empname()
        self.se.Enter_EmpName("David")
        self.log.info("Entering EmployeeName--->>")
        time.sleep(5)
        self.se.Click_on_SearchButton()
        self.log.info("Clicking on SeachButton -->>")
        #time.sleep(5)
        #print(self.se.Search_Result())
        time.sleep(5)
        if self.se.Search_Result() == True:
            self.log.info("search results Found")
            self.log.info("test_searchemp_006 TestCase is passed.")
            self.lp.Click_menu()
            self.log.info("Clicking on Menu_Button")

            self.lp.Click_logout()
            self.log.info("Clicking on Logout Button")

            assert True

        else:
            self.log.info("search results Not Found")
            self.lp.Click_menu()
            self.log.info("Clicking on Menu_Button")

            self.lp.Click_logout()
            self.log.info("Clicking on Logout Button")

            self.log.info("test_searchemp_006 TestCase is failed.")
            assert False
        self.driver.close()