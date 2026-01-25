cookies=driver.get_cookies()
print(len(cookies))
for cookie in cookies:
    print(cookie.get('name'))
#adding the cookie
driver.add_cookie({"name":"anurag","value":"12203"})
#deleting new cookie
driver.delete_all_cookies()
driver.delete_cookie("anurag")
