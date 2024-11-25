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


#Amazon logo:
driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo")


#Create account header:
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")


#Your name field:
driver.find_element(By.CSS_SELECTOR,".a-input-text.a-span12.auth-autofocus.auth-required-field.a-form-error")


#Mobile number or Email field:
driver.find_element(By.CSS_SELECTOR,"#ap_email")


#Password field:
driver.find_element(By.CSS_SELECTOR,"input#ap_password")


#Re-enter password:
driver.find_element(By.CSS_SELECTOR,"input#ap_password_check.a-input-text")


#Continue button:
driver.find_element(By.CSS_SELECTOR,"[aria-describedby='legalTextRow']")


#Conditions of Use link:
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_condition_of_use']")


#Privacy Notice link:
driver.find_element(By.CSS_SELECTOR,"[href*='notification_privacy_notice?']")

#Sign in link:
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")