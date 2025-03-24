from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://campus.w3schools.com/collections/certifications'

# Open the webpage
driver.get(url)

# Wait for page to load (optional)
driver.implicitly_wait(10)

# Prepare the CSV file to store course details
csv_filename = 'w3schools_certifications.csv'
with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Course Name', 'Cost'])  # Write header row

    # Find all course elements
    courses = driver.find_elements(By.CLASS_NAME, 'grid-product__title')  # Adjust class names if needed
    prices = driver.find_elements(By.CLASS_NAME, 'price')  # Adjust class names if needed

    # Loop through courses and prices
    for course, price in zip(courses, prices):
        course_name = course.text.strip() if course else "No course name found"
        cost = price.text.strip() if price else "No cost found"

        # Print and save to CSV
        print(f"Course Name: {course_name}")
        print(f"Cost: {cost}")
        csv_writer.writerow([course_name, cost])

# Close the browser
driver.quit()
