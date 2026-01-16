from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
print(driver.title)
print(driver.page_source)
print(driver.current_url)
print(driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]').text)
#text will always returns the inner text of the element <>inner text</>

print(driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]').get_attribute('class'))