from selenium import webdriver
# the following import will give us access to functionality such as the enter key, the escape key, etc.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# prints out the page's entire source code
# print(driver.page_source)

# asynchronous control structure:
try:
    main = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except:  
    driver.quit()

time.sleep(5) # pauses program for 5 seconds
driver.quit()






