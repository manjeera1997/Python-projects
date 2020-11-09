url = "https://www.ndtv.com/coronavirus/india-covid-19-tracker"
import requests  #import requests library
page = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text)
soup.title
soup.table
table = soup.find_all('table')
rows = table[0].find_all('tr')
[i.text for i in rows[0]]
[i.text.replace('\n','') for i in rows[0]]
[i.text.replace('\n','').strip() for i in rows[0]]
headings = [i.text.replace('\n','').strip() for i in rows[0]]
rows = table[0].find_all('tr')
for i in rows:
    print(i)
all_rows = []
for i in rows:
    td = i.find_all('td')
    row = [i.text for i in td]
    all_rows.append(row)
all_rows.pop(0)
for i in all_rows:
    i[0] = i[0][:i[0].find("DistrictCases")]
for i in all_rows:
    i[1] = i[1][:i[1].find(" ")]
    i[2] = i[2][:i[2].find(" ")]
    i[3] = i[3][:i[3].find(" ")]
    i[4] = i[4][:i[4].find(" ")]
import pandas as pd
data = pd.DataFrame(all_rows,columns=headings)
print(data)
