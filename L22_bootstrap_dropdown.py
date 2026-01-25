from pycparser.c_ast import Break
from selenium .webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()



#when there is no select class to dropdown then we use common xpath to identify the option
countries_list=driver.find_elements(By.XPATH,"//ul[@id=['select']/li")
for country in countries_list:
    if country.text== "india":
        country.click()
        break