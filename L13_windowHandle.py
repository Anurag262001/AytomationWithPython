from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")

driver.maximize_window()
wait = WebDriverWait(driver, 10)
username = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
driver.implicitly_wait(10)
username.send_keys("Admin")
driver.implicitly_wait(10)
#driver.current_window_handle  -->return windowID of single window
#driver.window_handles --> returns multiple windowID
print(driver.current_window_handle)
all_wins=driver.window_handles()
for win in all_wins:
    driver.switch_to.window(win)
    print(driver.title)
    if driver.title=="parent window":
        driver.switch_to.window(win)
        driver.close()


#tasks
#clicks all the links
#go to every browser
#get the title of all the browser
#close all the browsers