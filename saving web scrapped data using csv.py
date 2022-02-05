#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://brainyquote.com/topics/motivational-quotes"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'quotesList'}) 

for row in table.findAll('div', attrs = {'class':'qti-listm'}):
    quote = {}
    try:
        quote['author'] = row.img['alt'].split("-")[1]
        quote['text'] = row.img['alt'].split("-")[0]
        quotes.append(quote)   
        print(quote)
    except TypeError:
      continue 

fileName = 'quotes.csv'

with open(fileName,'w',newline='')as f:
    w = csv.DictWriter(f,['author','text'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
