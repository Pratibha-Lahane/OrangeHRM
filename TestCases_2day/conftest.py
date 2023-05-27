import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    # driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    return driver

def pytest_metadata(metadata):
    ##to add
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHrm"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Credence"
    ##Remove
    metadata.pop("Packages",None)
    metadata.pop("Plugins",None)

@pytest.fixture(params=[
    ("Admin","admin123","pass"),
    ("Admin1","admin123","fail"),
    ("Admin","admin1234","fail"),
    ("Admin1","admin1234","fail")
])
def getDataforlogin(request):
    return request.param

@pytest.fixture(params=[
    ("Komal","Vishal","Mande","pass"),
    ("","Abc","Xyz","fail"),
    ("Admin","","Xyz","fail"),
    ("Admin1","admin1234","","fail"),
    ("","","Admin","fail"),
    ("","admin1234","","fail"),
    ("Admin1","","","fail"),
    (" "," "," ","fail")
])
def getDataforAddemp(request):
    return request.param







