import pyfiglet
text=pyfiglet.figlet_format("Scrapper")
print(text)
print("Welcome to my new tool")
print("Please enter your correct info otherwise tool is auto close...")
gender=input("Enter your gender.. ")
if gender=="boy":
    print("hello Legend")
name=input("Enter your name.. ")
print("Hello.." + name)    
print("This tool is only for educational purpose.. developer is not responsible for your illegal activities.. ")    
import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <a> tags (links) in the HTML
        links = soup.find_all('a')
        
        # Extract and print the href attribute from each <a> tag
        for link in links:
            href = link.get('href')
            if href:
                print(href)
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)

def main():
    url = input("Enter the URL of the webpage to scrape: ")
    print("Scraping links from", url)
    scrape_links(url)

if __name__ == "__main__":
    main()

