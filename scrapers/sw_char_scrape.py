from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sw_book_scrape import driver


class CharacterDetails:
    def __init__(self, character):
        self.character = character

    def get_character(self):
        # access Youtini search page
        driver.get("https://starwars.fandom.com/wiki/Special:Search?query=&scope=internal&navigationSearch=true")

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

    def character_img(self):
        pass