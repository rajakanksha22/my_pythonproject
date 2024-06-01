
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
import re
#step 1:get the html 
# step 2: parse the html
# step 3: html tree traversal

def get_wikipedia_page(url):#to get the url support we use get
    response = requests.get(url)
    response.raise_for_status()
    return response.text
## to get all the paragraphs from  the page ,divs , anchor tags

def parse_wikipedia_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    ###title
    title = soup.find('h1', {'id':'firstHeading'}).text
    first_paragraph = soup.find('div',{'class':'mw-parser-output'}).find('p').text
##provided links ## to get all the links on the page;
    external_links=[]
    for link in soup.find_all('a',href=True):
        href=link['href']
        if re.match(r'^http[s]?://', href):
            external_links.append(href)
    images=[]
    for img in soup.find_all('img'):
        img_url='https:'+ img['src']
        alt_text=img.get('alt','No alt text available')
        images.append({'url': img_url,'alt_text':alt_text})

    return{
        'title':title,
        'first_paragraph':first_paragraph,
        'external_links':external_links,
        'images':images
    }

def scrape_wikipedia_page(url):
    html = get_wikipedia_page(url)
    return parse_wikipedia_page(html)

