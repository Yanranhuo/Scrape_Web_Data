# scrape-web-data

#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar 
#to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
#look at the "span" tag,got the number
sum = 0
for tag in tags:
	sum = sum + int(tag.contents[0])
	#print the content of that tag
    #Look at the parts of a tag
    #print('URL:', tag.get('span', None))
print(sum)
    
  
	
	
