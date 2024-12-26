#selenium playground table search demo
from selenium import webdriver
from selenium.webdriver.common.by import By

text_to_validate="Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

driver = webdriver.Firefox()
driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
driver.maximize_window()



print("title :", driver.title)

search=driver.find_element(By.XPATH,"//input[@type='search']")
#driver.find_elements(By.XPATH,"//input[@type='search']").send_keys("New York")
search.click()
search.send_keys("New York")

count = driver.find_element(By.XPATH,"//*[@id='example_info']")
text_from_browser= count.text
print(text_from_browser)

if(text_from_browser==text_to_validate):
    print("TEST CASE IS PASSED")
else:
    print("TEST CASE IS FAILED")

driver.close()



