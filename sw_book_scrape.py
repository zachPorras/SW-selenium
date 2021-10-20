from sw_scrape_driver import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class BookDetails:
    """
    This class allows user to retrieve Star Wars book details 
    from Youtini.com website, via selenium web scraping tool.

    Attributes:
        book (str): Star Wars book title
    
    Methods**:
        book_all_details(): Calls all methods to retrieve all book details

        get_book(): Instantiates webdriver & initial book search to find 
            book page

        book_author(): Retrieves book author.

        book_score(): Retrieves Youtini Book Score, graded on a scale 
        from 0-10.0, along with 1-word score category.

        book_verdict(): Retrieves a brief single sentence description.

        book_summary(): Retrieves Publisher Summary.

        book_img(): Retrieves url to book cover image.

        **All methods have the driver.quit() method commented out.
            This is for testing individual methods, since
            webdriver requires .quit() to stop running.
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
        # Youtini Publisher Summaries are constructed in two ways within HTML:
            # scenario 1 has summary text within p elements that are children of a div
            # scenario 2 has summary text directly within div element itself

        print("\nPublisher Summary:")

        # scenario 1: locates publisher's summary p elements
        search = driver.find_elements(By.XPATH, '//h2[@id="Publisher-Summary"]/following::div[1]/p')
        if search:
            summary_list = [element.text for element in search]
            summary_1 = ""
            for text in summary_list:
                summary_1 += text + '\n\n'
            return summary_1

        # scenario 2: locate publisher's summary directly within div
        else:    
            search_2 = driver.find_element(By.XPATH, '//h2[@id="Publisher-Summary"]/following::div')
            summary_2 = driver.execute_script("return arguments[0].innerHTML;", search_2)
            return summary_2   

        # driver.quit()

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
        print(self.book_summary())
        driver.quit()
