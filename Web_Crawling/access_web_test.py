import nltk
import urllib2

from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Basketball'
raw = urllib2.urlopen(url).read().decode('utf8')

text = BeautifulSoup(raw).get_text()
tokens = word_tokenize(text)

# Get only words:
word_only_list_web = [word for word in tokens if word.isalpha()]
word_only_list_web


