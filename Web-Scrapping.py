####################
##import requests as rq
##
##r = rq.get('https://www.youtube.com')
##
##print(r)
##
##print(r.content)


####################
##import requests as rq
##
##r = rq.get('https://www.youtube.com')
##
##print(r.url)
##
##print(r.status_code)


####################
##import requests as rq
##from bs4 import BeautifulSoup
##
##r = rq.get('https://www.youtube.com')
##
##print(r)
##
##soup = BeautifulSoup(r.content, 'html.parser')
##
##print(soup.prettify())


####################
##import requests as rq
##from bs4 import BeautifulSoup
##
##r = rq.get('https://www.youtube.com')
##
##soup = BeautifulSoup(r.content, 'html.parser')
##
##print(soup.title)
##
##print(soup.title.name)
##
##print(soup.title.parent.name)

####################
import requests as rq
from bs4 import BeautifulSoup
import csv
 
r = rq.get('https://www.youtube.com')
 
soup = BeautifulSoup(r.content, 'html.parser')

link_list = []
count = 1

for link in soup.find_all('a'):
    src = link.get('href')
    link_list.append({"src": src})
    count = count + 1
## creating csv files 
filename = 'links.csv'
with open(filename, 'w', newline = '') as f:
        w = csv.DictWriter(f,['src'])
        w.writeheader()
        w.writerows(link_list)


####################
##import requests as rq
##from bs4 import BeautifulSoup
##
##
### Making a GET request
##r = rq.get('https://www.youtube.com')
##
### Parsing the HTML
##soup = BeautifulSoup(r.content, 'html.parser')
##
##images_list = []
##
##images = soup.select('img')
##for image in images:
##	src = image.get('src')
##	alt = image.get('alt')
##	images_list.append({"src": src, "alt": alt})
##	
##for image in images_list:
##	print(image)



