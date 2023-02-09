import requests
from bs4 import BeautifulSoup
import os

url = input("Enter the URL: ")

# Request the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Get the current working directory
    cwd = os.getcwd()

    # Create a directory named `clone` to store the files
    dir_path = os.path.join(cwd, "clone")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Download all the files
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("http"):
            # Name the file `duplicate`
            file_path = os.path.join(dir_path, "duplicate")

            # Download the file
            file_response = requests.get(href)
            with open(file_path, "wb") as f:
                f.write(file_response.content)
else:
    print("Couldn't reach the URL")
