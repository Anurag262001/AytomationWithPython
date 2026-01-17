import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://saucedemo.com")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"google.com")
driver.find_element(By.PARTIAL_LINK_TEXT,"google.com")
all_achor_tags=driver.find_elements(By.TAG_NAME,"a")
print(len(all_achor_tags))
for link in all_achor_tags:
    print(link.text)


#check the number of brokenlink
links=driver.find_elements(By.TAG_NAME,"a")
count=0
for link in links:
    url=link.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print("broken link",url)
        count=count+1
    else:
        print("valid link",url)