from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
driver.maximize_window()
selected_elements =driver.find_element(By.XPATH," ")
item=Select(selected_elements)
item.select_by_index(0)
item.select_by_value(" ")
item.select_by_visible_text(" ")

#print all the options present in select
selected_elements =driver.find_element(By.XPATH," ")
item=Select(selected_elements)
all_options = item.options
print(len(all_options))
for one_by_one in all_options:
    print(one_by_one.text)

#selecting the option without using the any inbuild function
selected_elements =driver.find_element(By.XPATH," ")
item=Select(selected_elements)
all_options = item.options
print(len(all_options))
for one_by_one in all_options:
    if one_by_one.text=="INDIA":
        one_by_one.click()