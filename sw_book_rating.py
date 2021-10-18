from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"C:\Users\porra\operator\misc\installs\chromedriver.exe")

driver = webdriver.Chrome(service=service)

# access Youtini search page
driver.get("https://www.youtini.com/search")


# What book are you looking for?
book = "Master and Apprentice"

# search for book using search form
search_1 = driver.find_element_by_id("search")
search_1.send_keys(f"{book} complete book details")
search_1.send_keys(Keys.RETURN)

driver.implicitly_wait(3)

# access first search result
search_2 = driver.find_element_by_class_name("link")

# route to href attribute
book_href = search_2.get_attribute("href")
driver.get(f'{book_href}')

# locates review score
search_3 = driver.find_element_by_class_name("review-score-prof.header")
score = driver.execute_script("return arguments[0].innerHTML;", search_3)
print(f'The score for {book} is ' + score)

# time.sleep(5)

driver.quit()