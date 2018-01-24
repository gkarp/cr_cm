from bs4 import BeautifulSoup
import requests 
from clan import CLAN

stats_royale_url = "http://statsroyale.com/clan/"

clan_url = stats_royale_url + CLAN
#r = requests.get(clan_url)
#html_doc = r.text

with open("test_html.html", encoding="utf8") as f:
    html_doc = f.read()
	
soup = BeautifulSoup(html_doc, "html.parser")

data = soup.find_all("div", class_="clan__rowContainer")
print(data[0])
# for d in data:
#    print(d)
members = {}
keys = ["Rank", "Name", "Level", "League", "Trophies", "Crowns", "Donations", "Role"]
i = 0

'''
for d in data:
    member_data = d.find_all("div", class_="clan__row")
    for col in member_data:
        print(keys[i] + " = " + col.get_text())
        i = i + 1
    i = 0
'''
member_data = data[0].find_all("div", class_="clan__row")
for col in member_data:
    print(keys[i] + " = " + col.get_text().strip())
    i = i + 1
    


