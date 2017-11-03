# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random


url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)


print soup.title.string
file = open("MarriageQuotes.txt", "w+")
file.write("")

quotes = soup.findAll("p", attrs={"class": "quoteContent"})

i = 1

for i in random.sample(quotes, 5):
    five_quotes_sting = i.string.lstrip(' ')
    print five_quotes_sting
    file.write(five_quotes_sting + "\n")

file.close()
