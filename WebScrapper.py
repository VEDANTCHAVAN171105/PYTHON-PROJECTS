import requests
from bs4 import BeautifulSoup
import re  # Add import statement for the 're' module

def scrape_section_headings(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Print the response status code
    print("Response Status Code:", response.status_code)
    
    # Checking
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the section headings
        headings = soup.find_all(re.compile('^h[1-6]$'))  # Matches h1, h2, ..., h6
        
        # Print the section headings
        for heading in headings:
            print(heading.text.strip())
    else:
        print("Failed to retrieve section headings")

# URL of the website to scrape
url = 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe'

# Call the function to scrape section headings
scrape_section_headings(url)