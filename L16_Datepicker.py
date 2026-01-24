from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()
driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("01/24/2026")


#but some of the datepick dont take the date directly
driver.find_element(By.XPATH,'//*[@id="datepicker"]').clear()
year="2027"
month="January"
date="26"


while True:

    in_cal_month=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    in_cal_year=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text

    print(in_cal_year,in_cal_month)
    if in_cal_year==year and in_cal_month==month:
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]/span').click()
dates=driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for d in dates:
    if d.text==date:
        d.click()
        break
driver.implicitly_wait(50)