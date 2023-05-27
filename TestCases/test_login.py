# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#This is commented for PyCharm fetch function
#
#
# class Test_Login:
#
#
#     def test_login_001(self):
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(5)
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#         driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
#         driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
#         driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#
#         try:
#             driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
#             print("test_login_001 TestCase is pass")
#
#             driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
#             driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#             assert True
#         except NoSuchElementException:
#
#             print("test_login_001 Testcase is fail")
#             assert False
#
#
#
#
