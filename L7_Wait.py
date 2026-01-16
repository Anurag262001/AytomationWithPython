#implicit wait  //dynamic
#explicit wait  //dynamic
#time.sleep(5)  //static wait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
#to maximize the window
driver.maximize_window()

driver.implicitly_wait(10) #this wait will work for the entire line if there is no wait need then it wont wait but if there is any element that is not visible it will take 10seconds to locate that element if fond then it will continue to go to the next step

