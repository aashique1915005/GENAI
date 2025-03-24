from bs4 import BeautifulSoup
import requests
import csv

# URL to scrape
url = 'https://www.w3schools.com/html/'

# Prepare the CSV file
csv_filename = 'certificate_course_details.csv'
with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header row
    csv_writer.writerow(['Link', 'Course Name', 'Fees'])

    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all the links on the page
        links = soup.find_all('a', href=True)

        # Filter and process links containing "certification"
        certification_links = [link['href'] for link in links if 'certification' in link['href'].lower()]
        print("\nCertification Links Found:")
        for cert_link in certification_links:
            print("-", cert_link)

            # Ensure the link is absolute (if it's a relative URL, make it absolute)
            if not cert_link.startswith('http'):
                cert_link = requests.compat.urljoin(url, cert_link)

            # Fetch the certification page details
            cert_response = requests.get(cert_link)
            if cert_response.status_code == 200:
                cert_soup = BeautifulSoup(cert_response.text, 'html.parser')

                # Extract the course name and fees (Adjust tags/classes as per HTML structure)
                course_name = cert_soup.find('h1').get_text(strip=True) if cert_soup.find('h1') else "No course name found"
                fees_section = cert_soup.find('div', class_='fees')  # Replace 'div' and 'fees' with actual tags/classes
                fees = fees_section.get_text(strip=True) if fees_section else "No fees found"
                print(f"\nDetails from {cert_link}:")
                print(f"Course Name: {course_name}")
                print(f"Fees: {fees}\n")

                # Write details to the CSV file
                csv_writer.writerow([cert_link, course_name, fees])
            else:
                print(f"Failed to fetch {cert_link}. Status Code: {cert_response.status_code}")
    else:
        print(f"Failed to fetch the main webpage. Status Code: {response.status_code}")
