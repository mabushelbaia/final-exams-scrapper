# extract the table in index.html file with utf-8 encoding
from bs4 import BeautifulSoup
import pandas as pd
from ics import Calendar, Event
from datetime import datetime, timedelta

html_doc = open("index.html", encoding="utf-8").read()
soup = BeautifulSoup(html_doc, "lxml")
tables = soup.find_all("table")
table = tables[1]
# extract the table header
table_header = []
for th in table.find_all("th"):
    table_header.append(th.text.strip())
table_body = []
for tr in table.find_all("tr"):
    row = []
    for td in tr.find_all("td"):
        row.append(td.text.strip())
    if row:
        table_body.append(row)
# convert the table to pandas dataframe
df = pd.DataFrame(table_body, columns=table_header)
print(df)
# convert the datafram into a calender events in ics format
c = Calendar()
for index, row in df.iterrows():
    e = Event()
    e.name = "FINAL: " + row["Course"] + " " + row["Course Title"]
    # parse the date and time from the table knowing its in 24 hour formatp

    e.begin = datetime.strptime(
        row["Date"].split()[1] + " " + row["Time"].split("-")[0].strip(),
        "%d/%m/%Y %H:%M",
    )
    e.end = datetime.strptime(
        row["Date"].split()[1] + " " + row["Time"].split("-")[1].strip(),
        "%d/%m/%Y %H:%M",
    )
    e.location = row["Rooms"]
    c.events.add(e)
print(c)
with open("finals.ics", "w") as my_file:
    my_file.writelines(c)
