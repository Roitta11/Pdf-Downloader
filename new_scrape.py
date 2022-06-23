
'''
Plan for the project:

1) Get the url and create a Beautiful soup object
2) Parse the beautiful soup object and separate the links
3) Put the links in an index
4) Slice through the links to separate the summer and the winter papers
5) Use conditional statements to open the files for writing
6) Join the links in the folders 

'''

import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# The link from where the files are to be downloaded
source = "https://papers.gceguide.com/A%20Levels/Computing%20(9691)/"

# Use the current directory as the folder for downloading the files
folder_location = os.getcwd()

# Create two separate folder for storing the files
os.makedirs ("summer_files")
os.makedirs ("winter_files")

# Get the response and create a Beautiful soup object
response = requests.get(source)
soup = BeautifulSoup(response.text,'lxml')

# Parse the pdf links
pdf_link = soup.select("a[href$='.pdf']")

link_text=list()

# Keep a counter for the number of files 
counter = 0

for link in pdf_link:
    pdf_name = link['href'].split('/')[-1]

# Checking to separate the winter files from the summer files
    if "s" in pdf_name:
        filename = os.path.join(folder_location + "/summer_files/",link['href'].split('/')[-1])
    else:
        filename = os.path.join(folder_location + "/winter_files/",link['href'].split('/')[-1])
    

    with open(filename, 'wb') as file:
        # Downloading the files
        file.write(requests.get(urljoin(source,link['href'])).content)
        
    link_text.append(str(link.text))
 
    counter += 1

# The extreme limit for downloading all the files
    if counter == 700:
        break

    print(counter, "Downloading file named ",link['href'].split('/')[-1])

# Confirmation message of download
print("All the files have been downloaded successfully!")
