#scrolling page
#two ways 1st is offset 2nd untill the element is not visible

#scroll by offset
driver.execute_script("window.scrollBy(0,30000)","")
value=driver.execute_script("return window.pageYoffset;")
print(value)

#2. Scroll down page till the element is visible
flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)  #5038.3330078125
