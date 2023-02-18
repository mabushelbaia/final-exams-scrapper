# extract the table in index.html file with utf-8 encoding
from bs4 import BeautifulSoup
import pandas as pd
from icalendar import Calendar, Event
from datetime import datetime

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
    e.add('summary', "FINAL: " + row["Course"] + " " + row["Course Title"])
    # parse the date and time from the table knowing its in 24 hour format
    begin_time = datetime.strptime(row["Time"].split("-")[0].strip(), "%H:%M").strftime("%I:%M %p")
    end_time = datetime.strptime(row["Time"].split("-")[1].strip(), "%H:%M").strftime("%I:%M %p")
    e.add('dtstart', datetime.strptime(row["Date"].split()[1] + " " + begin_time, "%d/%m/%Y %I:%M %p"))
    e.add('dtend', datetime.strptime(row["Date"].split()[1] + " " + end_time, "%d/%m/%Y %I:%M %p"))
    e.add('location', row["Rooms"])
    c.add_component(e)

with open("finals.ics", "wb") as f:
    f.write(c.to_ical())  
