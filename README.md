# SW-selenium

This program utilizes Selenium web scraper to find information about Star Wars books from the Youtini website.

This will ultimately be folded into my Mos Eisley web application to create a more robust book storage feature,
so that various book details can be presented to the user automatically.

Current functionality includes:
- Book Author
- Youtini Book Score
- Book Verdict
- Publisher Summary
- Book Cover Image

There is an additional feature that will scrape character data from Fandom.Wookiepedia, but this is not yet functionable. These files include:
- sw_char_scrape.py
- test_char_scrape.py

All book functionality is housed in the BookDetails class. 

Calling the book_all_details method will sequentially trigger all individual methods in order to return all of the data listed above.

Individual methods can be called as needed for the specific needs of a parent application and for further testing during future changes & upgrades.

Testing can be conducted in test_XXXXX_scrape.py



p.s. this is useful - https://devhints.io/xpath
