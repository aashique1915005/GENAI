from bs4 import BeautifulSoup
import requests

# URL to scrape
url = 'https://www.w3schools.com/html/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract the titles of the sections in the HTML tutorial
    section_titles = soup.find_all('h2')
    print("Section Titles on the Page:")
    for title in section_titles:
        print("-", title.get_text())

    # Example: Extract all the links on the page
    links = soup.find_all('a', href=True)
    print("\nLinks on the Page:")
    for link in links:
        print("-", link['href'])
else:
    print(f"Failed to fetch the webpage. Status Code: {response.status_code}")
