#if you want to scrap a website:
#1.use the api 
#HTML Web scrapping using some tools like beautifulsoups
#installing all the requirements -
#pip install requests
#pip install bs4
#pip install html5lib

# commonly used objects (tag,navigable string BeautifulSoup, comments )

import requests
from bs4 import BeautifulSoup
url ="https://www.wikipedia.org/"
#step 1:get the html 
r =requests.get(url)#to get the url support we use get
htmlContent = r.content
#print(htmlContent)

# step 2: parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
#print (soup.prettify)
markup = "<p><!--this is a comment  --></p>"
soup2= BeautifulSoup(markup)
print(soup2.p.string)
exit()
# step 3: html tree traversal
title =soup.title
#print(title)

## to get all the paragraphs from  the page ,divs , anchor tags 
paras =soup.find_all('p')
anchors = soup.find_all('a') 
#get the text  from the text 
print(soup.find('p').get_text())
all_links=set()

## to get all the links on the page;
for link in anchors:
    if(link.get('href') != '#'):
        linkText =("https://www.wikipedia.org/"+link.get('href'))
all_links.add(linkText)
print(linkText)

 


