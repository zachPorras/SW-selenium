from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# global webdriver options
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
service = Service(r"C:\Users\porra\operator\misc\installs\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


class CharacterDetails:
    def __init__(self, character):
        self.character = character

    def get_character(self):
        pass

    def character_img(self):
        pass


class BookDetails:
    """
    This class allows user to retrieve Star Wars book details 
    from Youtini.com website, via selenium web scraping tool.

    Attributes:
        book (str): Star Wars book title
    
    Methods:
        book_all_details(): Calls all methods to retrieve all book details

        get_book(): Instantiates webdriver & initial book search to find book page

        book_author(): Retrieves book author.

        book_score(): Retrieves Youtini Book Score, graded on a scale from 0-10.0, 
            along with 1-word score category.

        book_verdict(): Retrieves a brief single sentence description.

        book_summary(): Retrieves Publisher Summary.

        book_img(): Retrieves url to book cover image.

    """
    def __init__(self, book):
        self.book = book

    def get_book(self):
        # access Youtini search page
        driver.get("https://www.youtini.com/search")

        # search for book using search form
        search_1 = driver.find_element(By.ID, 'search')
        search_1.send_keys(f"{self.book} complete book details")
        search_1.send_keys(Keys.RETURN)

        # access first search result (first instance of .link)
        search_2 = driver.find_element(By.CLASS_NAME, 'link')

        # route to href attribute i.e. book page
        book_href = search_2.get_attribute("href")
        driver.get(f'{book_href}')
        # driver.quit()
    
    def book_author(self):
        # locates author
        search = driver.find_element(By.XPATH, '//div[@class="author-prof"]/div[2]')
        
        # driver.quit()
        return f'\nAuthor: ' + search.text

    def book_score(self):
        # locates book score
        search = driver.find_element(By.CLASS_NAME, 'review-score-prof.header')
        score = driver.execute_script("return arguments[0].innerHTML;", search)
        search = driver.find_element(By.CLASS_NAME, 'text-block-149')
        score_text = driver.execute_script("return arguments[0].innerHTML;", search)

        # driver.quit()
        return f'\nYoutini Book Score: ' + score + " - " + score_text
    
    def book_verdict(self):
        # locates verdict
        search = driver.find_element(By.CLASS_NAME, 'verdict-prof-header')

        # driver.quit()
        return f'\nVerdict: ' + search.text

    def book_summary(self):
        # locates publisher's summary p elements
        search = driver.find_elements(By.XPATH, '//h2[@id="Publisher-Summary"]/following::div[1]/child::p')
        print("\nPublisher Summary:")
        
        # append all elements found to list
        summary_list = [element.text for element in search]

        # driver.quit()
        return summary_list

    def book_img(self):
        # locates img
        search = driver.find_element(By.XPATH, '//img[@class="image-84"]')
        book_img = search.get_attribute("src")

        # driver.quit()
        return f'\n{book_img}'

    def book_all_details(self):
        self.get_book()
        print(f'"{self.book}"')
        print(self.book_author())
        print(self.book_score())
        print(self.book_verdict())
        print(self.book_img())
        for p in self.book_summary():
            print(f'\n{p}')
        driver.quit()

        