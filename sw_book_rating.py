from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


class BookDetails:
    def __init__(self, book):
        self.book = book
        self.service = Service(r"C:\Users\porra\operator\misc\installs\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)

    def book_test(self):
        return self.book

    def get_book(self):
        driver = self.driver

        # access Youtini search page
        self.driver.get("https://www.youtini.com/search")

        # search for book using search form
        search_1 = self.driver.find_element_by_id("search")
        search_1.send_keys(f"{self.book} complete book details")
        search_1.send_keys(Keys.RETURN)

        # slight pause for html to load
        driver.implicitly_wait(0.5)

        # access first search result
        search_2 = driver.find_element_by_class_name("link")

        # route to href attribute i.e. book page
        book_href = search_2.get_attribute("href")
        driver.get(f'{book_href}')

    def book_score(self):
        self.get_book()
        driver = self.driver

        # locates review score
        search_3 = driver.find_element_by_class_name("review-score-prof.header")
        score = driver.execute_script("return arguments[0].innerHTML;", search_3)
        driver.quit()
        return f'The score for {self.book} is ' + score

        
chosen_book = "Lost Stars"
my_deets = BookDetails(chosen_book)
print(my_deets.book_score())
