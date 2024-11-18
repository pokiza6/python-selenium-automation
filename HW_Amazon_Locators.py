from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Find element 'Amazon Logo', by XPATH
driver.find_element(By.XPATH, "//i[@role='img' and @aria-label='Amazon']")

# Find element 'email field', by ID
driver.find_element(By.ID, "//input[@id='ap_email']")

#Find element 'Continue button',by multiple attr:
driver.find_element(By.XPATH, "//input[@aria-describedby='legalTextRow' and @type='submit']")

driver.find_element(By.XPATH, "//select[@aria-describedby='searchDropdownDescription']")



#Find element 'Need help?',by XPATH,partial and attr:
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt' and contains(text(),'Need help?')]")

#Find element 'Forgot your password?',by ID:
driver.find_element(By.ID,"//a[@id='auth-fpp-link-bottom']")

#Find element 'More ways to get support',by ID:
driver.find_element(By.ID,"//a[@id='ap-other-signin-issues-link']")

#Find element 'Create your Amazon account button',by ID:
driver.find_element(By.ID,"//a[@id='createAccountSubmit']")
