# IMDB-twitter-sentiment-analysis
Scrapes IMDB's celebrity birthday page and runs a twitter sentiment analysis.


# Problem Statement
IMDB provides a list of celebrities born on the current date. Below is the link: 
http://m.imdb.com/feature/bornondate
 
Get the list of these celebrities from this webpage using web scraping (the ones that are displayed i.e. top 10). You have to extract the below information: 

•	Name of the celebrity 
•	Celebrity Image
•	Profession
•	Best Work 

Once you have this list, run a sentiment analysis on twitter for each celebrity and finally the output should be in the below format 

•	Name of the celebrity: 
•	Celebrity Image: 
•	Profession: 
•	Best Work: 
•	Overall Sentiment on Twitter: Positive, Negative or Neutral 

# Tools and Packages Used
•	Python Version 3.7.1
•	Tweepy: is an open-sourced, easy-to-use Python library for accessing the Twitter API.
•	Codecs: Used for text encodings, which encode text to bytes, text to text and bytes to bytes.
•	String: To remove all punctuations from tweets.
•	BeautifulSoup (bs4): is a Python package for parsing HTML and XML documents. It is the module which scrapes the webpage. It automatically converts incoming documents to Unicode and outgoing documents to UTF-8.
•	Selenium: The webdriver kit emulates a web-browser and executes the JS scripts to load the dynamic content.

