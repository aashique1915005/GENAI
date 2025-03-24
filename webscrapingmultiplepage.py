# name of librarary to scrap website
from bs4 import BeautifulSoup
import requests
# is used to send request

# website = 'https://www.w3schools.com/html/default.asp'
# website = 'https://www.tcs.com/'
root = 'https://subslikescript.com'

website = f'{root}/movies'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content,'lxml')
# print(soup.prettify())

links = []
box = soup.find('article', class_='main-article')
for link in box.find_all('a',href=True):
    links.append(link['href'])

print(links)
for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)


# print(title)
# print(transcript)
#
