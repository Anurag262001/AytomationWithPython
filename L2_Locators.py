#xpath are of two types
#locators and Customized locators

#locators: id, name, Linktext, Class Name, Tag Name
#Customized: Css selectors(Tag and ID, Tag and Class, Tag and attribute, Tag class and attribute)
            #Xpath(absolute and relative)
            
# driver.find_element(By.ID," ")
# driver.find_element(By.NAME," ")
# driver.find_element(By.LINK_TEXT," ")
# driver.find_element(By.PARTIAL_LINK_TEXT," ")
# driver.find_element(By.CLASS_NAME," ")
# driver.find_element(By.TAG_NAME," ")
#To capture more than one elements in that case we use find_elements

#---------------CSS SELECTOR------------------#
# driver.find_element(By.CSS_SELECTOR,"input#idname")  here tagname i.e input # driver.find_element(By.CSS_SELECTOR,"#email")
# driver.find_element(By.CSS_SELECTOR,"input.classname")
# driver.find_element(By.CSS_SELECTOR,"input[attribute=value]") --> tag, attribute
# driver.find_element(By.CSS_SELECTOR,"input.classname[attribute=value]") -->tag,class name, attribute


