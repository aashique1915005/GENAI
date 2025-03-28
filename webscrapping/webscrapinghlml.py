import requests
from bs4 import BeautifulSoup

# Get the company name from the user
company = input("Enter the Company Name: ")

# Construct the Wikipedia URL
website = "https://en.wikipedia.org/wiki/"
formatted_url = website + company.replace(" ", "_")  # Replace spaces with underscores
print(f"Fetching data from: {formatted_url}")

try:
    # Make a GET request to fetch the content
    result = requests.get(formatted_url)
    result.raise_for_status()  # Raise an error for invalid HTTP responses

    # Parse the HTML content
    soup = BeautifulSoup(result.text, 'lxml')

    # Extract the first three <p> elements
    paragraphs = soup.find_all('p', limit=3)  # Limit to the first 3 <p> elements
    combined_text = " ".join([p.text.strip() for p in paragraphs if p.text.strip()])

    if combined_text:
        print("\nCombined Paragraph:")
        print(combined_text)
    else:
        print("Could not extract meaningful content from the first three paragraphs.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")