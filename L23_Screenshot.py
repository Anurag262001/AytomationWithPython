import os
from selenium .webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.save_screenshot("/home/user/Desktop/screenshot.png")
driver.get_screenshot_as_png(os.getcwd()+"\\sreenshot.png")
driver.quit()