import requests 
from bs4 import BeautifulSoup

url = "https://brainyquote.com/topics/motivational-quotes"

#step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent , 'html.parser')
#print(soup.prettify)

#step 3 html tree traversal

#commonly used types of objects:
#print(type(title)) #1. tag
#print(type(title.string)) #2.Navigable String
#print(type(soup)) #3. Beautiful soup
# #4. Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

#Get the title of the html page
title = soup.title

#Get all the paragraphs from the page 
paras = soup.find_all('p')
#print(paras)


#print(anchors)

#Get first element in the html page
print(soup.find('p'))

#Get classes of any element in the HTML page
#print(soup.find('p')['class'])

#find all the elements with class lead
#print(soup.find_all("p",class_="lead"))

# Get the text from the tags/soup
#print(soup.find('p').get_text())
print(soup.get_text())

#Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
#Get all the links on the page :
for link in anchors:
    if(link.get('href') != '#'):
        linktext ="https://brainyquote.com/topics/motivational-quotes" + link.get('href')
        all_links.add(link)
        #print(linktext)
        
