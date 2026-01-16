#implicit wait  //dynamic
#explicit wait  //dynamic
#time.sleep(5)  //static wait
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
#to maximize the window
driver.maximize_window()

driver.implicitly_wait(10) #this wait will work for the entire line if there is no wait need then it won't wait but if there is any element that is not visible it will take 10seconds to locate that element if fond then it will continue to go to the next step if not it will throw the exception in the code



#explicit wait 
exwait = WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])  #explicit wait decalration
track_element = exwait.until(EC.presence_of_element_located(By.XPATH," "))
track_element.click()