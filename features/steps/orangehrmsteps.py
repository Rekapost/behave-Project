from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@Given('Launch Chrome browser')
def launchBrowser(context):
    # context.driver=webdriver.Chrome(executable_path="C://Users//Reka//Drivers//chromedriver.exe")
    context.driver=webdriver.Chrome()

@when('open orangeHRM page')
def openHomePage(context):
    context.driver.get("https://www.orangehrm.com/")

@then('verify that the logo present on page')
def verifyLogo(context):
    status=context.driver.find_element(By.XPATH,"//img[@src='/_resources/themes/orangehrm/dist/images/OrangeHRM_Logo.svg']").is_displayed()
    assert status is True

@Then('close browser')
def closeBrowser(context):
    context.driver.close()


#   terminal:     behave 