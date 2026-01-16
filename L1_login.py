from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
#to maximize the window
driver.maximize_window()

driver.find_element(By.ID,'password').clear()
driver.find_element(By.ID,'password').send_keys("secret_sauce")

driver.find_element(By.ID,'user-name').clear()
driver.find_element(By.ID,'user-name').send_keys("standard_user")

driver.find_element(By.ID,'login-button').click()
#to get the title
title_page=driver.title
print(title_page)
expected_title="Swag Labs"
if expected_title==title_page:
    print("logged in")
else:
    print("unable to login")