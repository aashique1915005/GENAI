from bs4 import BeautifulSoup
import requests

# URL to scrape
url = 'https://campus.w3schools.com/collections/certifications'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Open a text file to save the course details
    with open('courses_and_prices.txt', 'w', encoding='utf-8') as file:
        file.write("Course Name and Original Price:\n")
        file.write("="*50 + "\n")

        # Locate course details (adjust the tag and class based on actual structure)
        courses = soup.find_all('div', class_='grid-product__title')  # Replace class name as needed
        prices = soup.find_all('span', class_='price')  # Replace class name as needed

        # Loop through courses and prices
        for course, price in zip(courses, prices):
            course_name = course.get_text(strip=True) if course else "No course name found"
            original_price = price.get_text(strip=True) if price else "No price found"

            # Write details to the file
            file.write(f"Course Name: {course_name}\n")
            file.write(f"Original Price: {original_price}\n")
            file.write("="*50 + "\n")

    print