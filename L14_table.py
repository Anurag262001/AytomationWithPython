#count number of rows and col
#read specific row and col data
#Read all cols and rows
#read data based on conditions

'''
<table name="booktable">
<Tbody>
<tr>
<th>
<th>
</tr>

<tr>
<td>
<td>
</tr>

<tr>
<td>
<td>
</tr>

<tr>
<td>
<td>
</tr>
</Tbody>
</table>
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#len of all the rows
rows=driver.find_elements(By.XPATH,'//table[@name="booktable]//tr')
print(len(rows))
#len of all the cols
#to find cols we simple find th
cols=driver.find_elements(By.XPATH,'//table[@name="booktable]//tr[1]/th')
print(len(cols))

#read specific row and col data
#this xpath will retrive 2nd row col 1 data
data=driver.find_element(By.XPATH,'//table[@name="booktable]//tr[2]/td[1]')


#Read all cols and rows
print("printing all the rows and columns data......................")
for r in range(2, len(rows)+1):
    for c in range(1, len(cols)+1):
        data = driver.find_element(
            By.XPATH,
            "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]"
        ).text
        print(data,end='   ')


#Read data based on the condition (List book name whose author is mukesh)
for r in range(2, no0fRows+1):
    authorName=driver.find_element(By.XPATH,"//table [@name='BookTable']/tbody/tr['+str(r)+']/td[2]").text
    if authorName=="Mukesh":
        bookName = driver.find_element(By.XPATH, "//table [@name='BookTable']/tbody/tr[' + str(r) +' ]/td[1]").text
    price = driver.find_element(By.XPATH, "//table [@name='BookTable']/tbody/tr[' + str(r) + ']/td[4]").text
    print(bookName," ",authorName," ",price)
