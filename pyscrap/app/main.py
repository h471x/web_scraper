import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
from os.path import abspath as abs, join as jn, dirname as dir
from importlib.metadata import version, PackageNotFoundError

# Hardcoded version when run as standalone
__version__ = "0.1"

def get_csv_file(csv_file):
    return jn(dir(abs(__file__)), "..", "scraped_data", csv_file)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Web scraper script.')
    parser.add_argument('-l', '--link', required=True, help='URL to scrape')
    parser.add_argument('-t', '--tag', required=True, help='HTML tag to scrape')
    
    # Add version argument
    parser.add_argument('-v', '--version', action='version', 
        version='%(prog)s ' + get_version()
    )

    args = parser.parse_args()

    # Get the URL and tag from the command-line arguments
    url = args.link
    tag = args.tag

    try:
        # Send a request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the specified tag
        elements = soup.find_all(tag)

        # Extract and store data
        data = []
        for element in elements:
            title = element.find('h2').text if element.find('h2') else "No title"
            link = element.find('a')['href'] if element.find('a') else "No link"
            data.append({'title': title, 'link': link})

        # Print the extracted data
        print("Scraped Data:")
        for entry in data:
            print(f"Title: {entry['title']}, Link: {entry['link']}")

        # Save the data to a CSV file
        df = pd.DataFrame(data)
        df.to_csv(get_csv_file('data.csv'), index=False)
        print("Data saved to data.csv")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)

def get_version():
    try:
        # If the package is installed, return its version
        return version('pyscrap-tool')
    except PackageNotFoundError:
        # If not, return the hardcoded version
        return __version__

if __name__ == '__main__':
    main()
