from bs4 import BeautifulSoup
import requests
import time

response = requests.get('https://en.wikipedia.org/wiki/Kreayshawn')

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify().encode("utf-8"))
#print(soup.find("div", class_="mw-parser-output")
#time.sleep(2)
content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        first_relative_link = element.find("a", recursive=False).get('href')
        break
print(first_relative_link)
# u'title'

#print(soup.title.string)
# u'The Dormouse's story'

#print(soup.title.parent.name)
# u'head'
