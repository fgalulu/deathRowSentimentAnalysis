import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
# create a handle, page to handle the contents of the website.
page = requests.get(url)

# store the contents of the website under soup.
# soup = lh.fromstring(page.content)
soup = BeautifulSoup(page.text, "lxml")

# parse data that are stored between <table> of html.
# tr_links = doc.xpath('//tr')[0].get("href")
tag = soup.table("a")

# defining variables and list
col = []
i = 0

# loop through the links, append the root url and store them in a list
for links in tag:
    link = links.get("href")
    # print(link)
    col.append('https://www.tdcj.texas.gov/death_row/' + link)

# spilt the links for last statement and inmate info.
col1 = col[::2]
col2 = col[1::2]
# print(col1)
# print(col2)

# list for last statements and information
laststatement = []

# for loop to open each last statement link and get desired page
for link in col2:
    webpage = requests.get(link)
    doc = BeautifulSoup(webpage.text, "lxml")
    row = []
    # print(doc)
    # use try to catch index error
    try:
        tag1 = doc("p")[5].string
        row.append(tag1)
    except IndexError:
        row.append('No Statement')
    try:
        tag2 = doc("p")[3].string
        row.append(tag2)
    except IndexError:
        row.append('error')

    laststatement.append(row)

print(len(laststatement))

# convert to dataframe
df = pd.DataFrame(laststatement)
print(df)
df.to_csv('last.csv', sep=';')
