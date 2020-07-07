from selenium import webdriver

PATH = "/Users/alanmarx/Program Files/chromedriver"
driver = webdriver.Chrome(PATH)

# running this file will open up the provided website: 
driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()