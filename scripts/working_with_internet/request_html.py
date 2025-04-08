import requests
from bs4 import BeautifulSoup

# BeautifulSoup documentation:
# https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Monaco"

# Fetch the HTML content using the requests module
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract the title of the page
    print("Page Title:")
    print(soup.title.string)
    
    # Example: Extract h1 headings
    print("\nHeadings:")
    for heading in soup.find_all(['h1']):
        print(heading.get_text())

    # Example: Extract the first link  
    link=soup.find('a')
    print("First link: ",link)
    print("Link text: ",link.get_text())
    print("Link href: ",link['href'])

    # Example: Extract element by class
    print("Element with class 'navbox-title':")
    element_by_class = soup.find(class_="navbox-title")
    if element_by_class:
        print(element_by_class.get_text())

    # Example: accessing parent and child elements
    first_ul = soup.find('ul')  # Find the first <p> tag
    if first_ul:
        print("First ul Content:")
        print(first_ul.get_text())
        
        print("Parent Element:")
        print(first_ul.parent.name)
        
        print("Child Elements:")
        for child in first_ul.children:
            print(child)

    # Example: Extract data from a table
    table = soup.find('table')
    print("Table Data:")
    if table:
        for row in table.find_all('tr'):
            cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
            print(cells)
    else:
        print("No table found on the page.")

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")