from selenium import webdriver
# the following import will give us access to functionality such as the enter key, the escape key, etc.
from selenium.webdriver.common.keys import Keys
import time


PATH = "/Users/alanmarx/Program Files/chromedriver"
driver = webdriver.Chrome(PATH)

# running this file will open up the provided website: 
driver.get("https://techwithtim.net")
print(driver.title)

# will find the first HTML element on the page with the name "s"
search = driver.find_element_by_name("s")
# will input the string "test" on the HTML element located above
search.send_keys("test")
# will hit the enter/return key after we have inputted the string
search.send_keys(Keys.RETURN)

# pauses the program for 5 seconds:
time.sleep(5)

driver.quit()