I am Learning the book <<Web Scraping with Python>>, this is the reading notes of this book.

from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read())
