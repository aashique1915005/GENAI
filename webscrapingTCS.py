from bs4 import BeautifulSoup
import requests

# Define the website URL
website = 'https://www.tcs.com/'
result = requests.get(website)
content = result.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Example: Extracting specific sections, e.g., titles and links
links = []
titles = []

# Find all sections or elements you want to scrape (e.g., anchor tags <a>)
for section in soup.find_all('a', href=True):
    title = section.get_text(strip=True)  # Text inside the anchor tag
    link = section['href']  # The 'href' attribute of the anchor tag
    if title and link:  # Avoid empty or unnecessary entries
        titles.append(title)
        links.append(link)

# Display the scraped data
for title, link in zip(titles, links):
    print(f"Title: {title}")
    print(f"Link: {link}")
    print('-' * 50)

# Save the data into a file (optional)
with open('tcs_links.txt', 'w', encoding='utf-8') as file:
    for title, link in zip(titles, links):
        file.write(f"Title: {title}\nLink: {link}\n{'-' * 50}\n")

print("Scraping complete. Check 'tcs_links.txt' for the saved data.")
