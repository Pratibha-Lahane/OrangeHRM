# import time
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
#
#
# class Test_AddEmp:
#
#     def test_addemp_002(self):
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(5)
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#         driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
#         driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
#         driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#
#         driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
#         driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
#         driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Komal")
#         driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("V")
#         driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("M")
#         #driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus'][normalize-space()='Employee Id']").send_keys("274") ###autogenerated emp id
#         #time.sleep(3)
#         driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
#         try:
#             driver.find_element(By.XPATH,"//h6[normalize-space()='Personal Details']")
#             print("test_addemp_002 TestCase is pass")
#             driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
#             driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#             assert True
#
#         except NoSuchElementException:
#             print("test_addemp_002 TestCase is Fail")
#             assert False
#
#
#
#
#
#
