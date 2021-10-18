# SW-selenium

This program utilizes Selenium web scraper to find information about Star Wars books from the Youtini website.

This will ultimately be folded into my Mos Eisley web application to create a more robust book storage feature,
so that various book details can be presented to the user automatically.

Current functionality includes:
- Youtini Book Score
- Book Verdict
- Publisher Summary **


All functionality is housed in the BookDetails class. 

Although there are a handful of methods within this class, 
calling the book_all_details method will trigger all individual methods in order to return all of the data listed above.

Individual methods can be called as needed for the specific needs of an application and for further testing during future changes & upgrades.


** Currently, some book pages have slightly different formatting which inhibits consistent element traversing. This functionality is still being worked on but is largely compatible with most book pages on Youtini.
