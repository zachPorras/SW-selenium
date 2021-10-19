from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BookDetails:
    """
    This class allows user to retrieve Star Wars book details 
    from Youtini.com website, via selenium web scraping tool.

    Attributes:
        book (str): Star Wars book title
    
    Methods:
        book_all_details(): Calls all methods to retrieve all book details
        get_book(): Instantiates webdriver & initial book search to find book page
        book_score(): Retrieves Youtini Book Score, graded on a scale from 0-10.0, 
            along with 1-word score category.
        book_verdict(): Retrieves a brief single sentence description.
        book_summary(): Retrieves Publisher Summary.

    """
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

    # def book_test(self):
    #     return self.book

    def get_book(self):
        driver = self.driver

        # access Youtini search page
        self.driver.get("https://www.youtini.com/search")

        # search for book using search form
        search_1 = self.driver.find_element(By.ID, 'search')
        search_1.send_keys(f"{self.book} complete book details")
        search_1.send_keys(Keys.RETURN)

        # access first search result
        search_2 = driver.find_element(By.CLASS_NAME, 'link')

        # route to href attribute i.e. book page
        book_href = search_2.get_attribute("href")
        driver.get(f'{book_href}')

    def book_score(self):
        self.get_book()
        driver = self.driver

        # locates book score
        search = driver.find_element(By.CLASS_NAME, 'review-score-prof.header')
        score = driver.execute_script("return arguments[0].innerHTML;", search)
        search = driver.find_element(By.CLASS_NAME, 'text-block-149')
        score_text = driver.execute_script("return arguments[0].innerHTML;", search)
        # driver.quit()
        return f'\nYoutini Book Score for "{self.book}": ' + score + " - " + score_text
    
    def book_verdict(self):
        self.get_book()
        driver = self.driver

        # locates verdict
        search = driver.find_element(By.CLASS_NAME, 'verdict-prof-header')
        verdict = driver.execute_script("return arguments[0].innerHTML;", search)
        # driver.quit()
        return f'\nVerdict: ' + verdict

    def book_summary(self):
        self.get_book()
        driver = self.driver

        # locates publisher's summary p elements
        search = driver.find_elements(By.XPATH, '//h2[@id="Publisher-Summary"]/following::div[1]/child::p')
        print("\nPublisher Summary:")
        
        # append all elements found to list
        summary_list = [element.text for element in search]

        driver.quit()
        return summary_list
    
    def book_all_details(self):
        print(self.book_score())
        print(self.book_verdict())
        for p in my_deets.book_summary():
            print(f'\n{p}')


# testing
chosen_book = "Lost Stars"
my_deets = BookDetails(chosen_book)

my_deets.book_all_details()

