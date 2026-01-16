from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
#to maximize the window
driver.maximize_window()
driver.get("https://youtube.com")
driver.maximize_window()
driver.back()
driver.forward()
driver.refresh()