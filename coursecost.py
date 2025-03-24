from bs4 import BeautifulSoup
import requests

# URL of the certification page
url = 'https://campus.w3schools.com/collections/certifications'

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Open a text file to save the course details
    with open('certification_details.txt', 'w', encoding='utf-8') as file:
        # Find all course sections (adjust the tag and class based on actual structure)
        courses = soup.find_all('div', class_='grid-product__title')  # Replace with actual class name
        prices = soup.find_all('span', class_='price')  # Replace with actual class name

        # Loop through courses and prices
        for course, price in zip(courses, prices):
            course_name = course.get_text(strip=True) if course else "No course name found"
            cost = price.get_text(strip=True) if price else "No cost found"

            # Write details to the text file
            file.write(f"Course Name: {course_name}\n")
            file.write(f"Cost: {cost}\n")
            file.write("="*50 + "\n")

    print("Course details have been successfully saved to certification_details.txt.")
else:
    print(f"Failed to fetch the webpage. Status Code: {response.status_code}")
