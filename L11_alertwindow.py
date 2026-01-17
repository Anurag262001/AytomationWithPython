from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,'//*[@id="OKTab"]/button').click()
alert_window=driver.switch_to.alert
print(alert_window.text)
alert_window.accept()
alert_window.dismiss()
#input in alert window
alert_window.send_keys("hi this side anurag")

#automentication popup
#popup where we have to enter the username and the password we have to bypass that popup syntax is

#-> ex original url: http://admin:admin@the-internet.herokuapp.com/basic_auth
#bypassing the syntax: http://the-internet.herokuapp.com/basic_auth
driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')