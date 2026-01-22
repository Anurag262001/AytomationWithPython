from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
rowlen=len(driver.find_elements(By.XPATH,"//table[@id='BookTable']//tbody/tr"))
count=0
for r in range(1,rowlen+1):
    status=driver.find_element(By.XPATH,"//table[@id='BookTable']//tbody/tr['+str(r)+']/td[1]").text
    if status=='Enabled':
        count+=1
print(rowlen)
print(count)
print(rowlen-count)
