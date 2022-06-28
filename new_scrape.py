
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

# source = "https://papers.gceguide.com/O%20Levels/Bengali%20(3204)/"

# Use the current directory as the folder for downloading the files
folder_location = os.getcwd()

# Create folders for storing the files
for i in range(2003, 2022):
    os.makedirs(folder_location + f"/{i}")


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
    if "3" in pdf_name:
        filename = os.path.join(folder_location + "/2003/",link['href'].split('/')[-1])
    elif "4" in pdf_name:
        filename = os.path.join(folder_location + "/2004/",link['href'].split('/')[-1])
    elif "5" in pdf_name:
        filename = os.path.join(folder_location + "/2005/",link['href'].split('/')[-1])
    elif "6" in pdf_name:
        filename = os.path.join(folder_location + "/2006/",link['href'].split('/')[-1])
    elif "7" in pdf_name:
        filename = os.path.join(folder_location + "/2007/",link['href'].split('/')[-1])
    elif "8" in pdf_name:
        filename = os.path.join(folder_location + "/2008/",link['href'].split('/')[-1])
    elif "9" in pdf_name:
        filename = os.path.join(folder_location + "/2009/",link['href'].split('/')[-1])
    elif "10" in pdf_name:
        filename = os.path.join(folder_location + "/2010/",link['href'].split('/')[-1])
    elif "11" in pdf_name:
        filename = os.path.join(folder_location + "/2011/",link['href'].split('/')[-1])
    elif "12" in pdf_name:
        filename = os.path.join(folder_location + "/2012/",link['href'].split('/')[-1])
    elif "13" in pdf_name:
        filename = os.path.join(folder_location + "/2013/",link['href'].split('/')[-1])
    elif "14" in pdf_name:
        filename = os.path.join(folder_location + "/2014/",link['href'].split('/')[-1])
    elif "15" in pdf_name:
        filename = os.path.join(folder_location + "/2015/",link['href'].split('/')[-1])
    elif "16" in pdf_name:
        filename = os.path.join(folder_location + "/2016/",link['href'].split('/')[-1])
    elif "17" in pdf_name:
        filename = os.path.join(folder_location + "/2017/",link['href'].split('/')[-1])
    elif "18" in pdf_name:
        filename = os.path.join(folder_location + "/2018/",link['href'].split('/')[-1])
    elif "19" in pdf_name:
        filename = os.path.join(folder_location + "/2019/",link['href'].split('/')[-1])
    elif "20" in pdf_name:
        filename = os.path.join(folder_location + "/2020/",link['href'].split('/')[-1])
    elif "21" in pdf_name:
        filename = os.path.join(folder_location + "/2021/",link['href'].split('/')[-1])
    else:
        filename = os.path.join(folder_location + "/2022/",link['href'].split('/')[-1])
    
    
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
