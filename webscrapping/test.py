import requests
from bs4 import BeautifulSoup


def scrape_cnbc(company_name):
    # Construct the URL dynamically
    url = f"https://www.cnbc.com/search/?query={company_name}&qsearchterm={company_name}"

    # Send a GET request to the CNBC search page
    response = requests.get(url)

    print (response)

    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #
    #     # Example: Extracting article titles and URLs
    #     articles = soup.find_all('div', class_='SearchResultCard')
    #     for article in articles:
    #         title = article.find('a').get_text(strip=True)
    #         link = article.find('a')['href']
    #         print(f"Title: {title}\nLink: {link}\n")
    # else:
    #     print(f"Failed to fetch data. Status code: {response.status_code}")


# Replace 'TCS' with the desired company name
scrape_cnbc("TCS")
