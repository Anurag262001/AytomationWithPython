import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,'//*[@id="tuesday"]').click()
time.sleep(10)

#select multiple checkbox alltogether
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
#approch1
for i in range (len(checkboxes)):
    checkboxes[i].click()
#approch2
for checkbox in checkboxes:
    checkbox.click()
#select multiple checkboxes on conditions
for checkbox in  checkboxes:
     weekname=checkbox.get_attribute('id')
     if(weekname=='monday' or weekname=='tuesday'):
         checkbox.click()
#selecting the last two element
#starting = total-from_last_elments
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()
#1st 2 elements
for i in range (len(checkboxes)):
    if i<2:
        checkboxes[i].click()
#clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()