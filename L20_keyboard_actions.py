from argparse import Action
from selenium.webdriver import Keys
from selenium import  webdriver
from selenium.webdriver.common.by import By
#copy and paste
driver=webdriver.Chromedriver()
input1=driver.find_element(By.ID,"input1")
input2=driver.find_element(By.ID,"input2")
act=Action(driver)
#copy
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB)
act.peform()

#paste
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
