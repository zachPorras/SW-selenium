from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class BookDetails:
    def __init__(self, book):
        self.book = book
        service = Service(r"C:\Users\porra\operator\misc\installs\chromedriver.exe")
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=service, options=self.options)

    def book_test(self):
        return self.book

    def get_book(self):
        driver = self.driver

        # access Youtini search page
        self.driver.get("https://www.youtini.com/search")

        # search for book using search form
        search_1 = self.driver.find_element(By.ID, 'search')
        search_1.send_keys(f"{self.book} complete book details")
        search_1.send_keys(Keys.RETURN)

        # slight pause for html to load
        # driver.implicitly_wait(0.5)

        # access first search result
        search_2 = driver.find_element(By.CLASS_NAME, 'link')

        # route to href attribute i.e. book page
        book_href = search_2.get_attribute("href")
        driver.get(f'{book_href}')

    def book_score(self):
        self.get_book()
        driver = self.driver

        # locates review score
        search = driver.find_element(By.CLASS_NAME, 'review-score-prof.header')
        score = driver.execute_script("return arguments[0].innerHTML;", search)
        driver.quit()
        return f'The Youtini Book Score for "{self.book}" is ' + score

    
    def book_verdict(self):
        self.get_book()
        driver = self.driver

        # locates preview
        search = driver.find_element(By.CLASS_NAME, 'verdict-prof-header')
        verdict = driver.execute_script("return arguments[0].innerHTML;", search)
        driver.quit()
        return f'Preview: ' + verdict

        
chosen_book = "Path of Destruction"
my_deets = BookDetails(chosen_book)
print(my_deets.book_score())
# print(my_deets.book_verdict())
