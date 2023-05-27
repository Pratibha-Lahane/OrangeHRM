import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_binary_path = "C:\\Users\\91702\\AppData\\Local\\Microsoft\\WindowsApps\\firefox.exe"

# Create a Service object
service = Service(executable_path="D:\Automation selinium\Driver\geckodriver.exe")

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = firefox_binary_path

# Start the WebDriver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Rest of your code...

#driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

