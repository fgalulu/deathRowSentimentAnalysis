import pandas as pd
import requests
import lxml.html as lh

url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
# soup = BeautifulSoup(requests.get(url).text, "html")

# create a handle, page to handle the contents of the website.
page = requests.get(url)
# store the contents of the website under doc.
doc = lh.fromstring(page.content)
# parse data that are stored between <tr> of html.
tr_elements = doc.xpath('//tr')

# open file
filename = "deathRow.csv"
f = open(filename, 'w')

# check length of the rows
[len(T) for T in tr_elements]

# create empty list
col = []
i = 0

# for each row, store each first element(header) and empty list
for td in tr_elements[0]:
    i += 1
    name = td.text_content()
    # print('%d: "%s"' % (i, name))
    col.append((name, []))

# Since out first row is the header, the data is stored on the second row onwards
for j in range(1, len(tr_elements)):
    T = tr_elements[j]
    # if row is not of size 10, the //tr data is not from our table
    if len(T) != 10:
        break

    # i is the index of our column
    i = 0

    # iterate through  each element of the row
    for t in T.iterchildren():
        data = t.text_content()
        # append the data to the empty list of the  i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i += 1

# print(col)

# convert to dictionary
Dict = {title: column for (title, column) in col}
df = pd.DataFrame(Dict)
print(df)
df.to_csv('deathRow.csv', mode='a', sep= ';')
