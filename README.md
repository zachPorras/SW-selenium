# SW-selenium

This program utilizes Selenium web scraper to find information about Star Wars books from Youtini.com, a website dedicated to the Star Wars Expanded Universe aka EU.

## Current functionality includes:
- Book Author
- Youtini Book Score
- Book Verdict
- Publisher Summary
- Book Cover Image

All book functionality is housed in the BookDetails class. 

Calling the book_all_details method will sequentially trigger all individual methods in order to return all of the data listed above.

Individual methods can be called as needed for the specific needs of a parent application and for further testing during future changes & upgrades. There are notes in the docstring regarding testing individual methods.

## Future work on this project:
- This will ultimately be folded into my Mos Eisley web application to create a more robust book storage feature,
so that various book details can be presented to the user automatically.
- I would like to pass a large list of books (Youtini has various resources available from which this could be extrapolated) into a BookDetails instance and save book data in a database. This could allow me to construct a reliable API for retrieving Star Wars book information, instead of relying on scraping a site that may change in the future.
- A new class that will scrape Star Wars character data from Fandom.Wookiepedia. These files currently exist but are not yet fully functionable.


<br>

### Hope you enjoy!

<br>

<em>May the force be with you</em> :milky_way:

 -- zP

<br>
