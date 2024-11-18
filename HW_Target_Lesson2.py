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
driver.maximize_window()

#Open URL:
driver.get('https://www.target.com/')

#Click sign in button:
driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]").click()
sleep(2)

#Click SignIn from side navigation:
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(2)

#Verify SignIn page opened. 'Sign into your Target account” text is shown:
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH,"//span[contains(text(),'Sign into your Target account')]")
print('Test passed')
