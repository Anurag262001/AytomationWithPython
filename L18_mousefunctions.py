#drag and drop
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver=webdriver.Chrome()
act=ActionChains(driver)
from_=driver.find_element(By.XPATH,'')
to=driver.find_element(By.XPATH,'')
act.drag_and_drop_by_offset(from_,to)
act.perform()
#mouse hover
act=ActionChains(driver)
act.move_to_element(webelement_xpath/name).perform()
act.perform()
#Rightclick
act=ActionChains(driver)
act.context_click(webelement_xpath/name).perform()
#doubleclick
act=ActionChains(driver)
act.context_click(webelement_xpath/name).perform()


