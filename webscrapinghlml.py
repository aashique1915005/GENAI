# name of librarary to scrap website
from bs4 import BeautifulSoup
import requests
# is used to send request

# website = 'https://www.w3schools.com/html/default.asp'
# website = 'https://www.tcs.com/'

website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')
# box = soup.find('article', class_='industry-heading')


title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator='  ')
print(title)
print(transcript)

with open('wrap.txt', 'w') as file:
    file.write(transcript)