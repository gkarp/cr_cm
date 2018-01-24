import requests 
from clan import CLAN
from sr_scraper import createDataFile

'''
This script will send a request to the statsroyale website for a specific Clash
Royale clan and then run the createDataFile script to scrape the request. 
'''

stats_royale_url = "http://statsroyale.com/clan/"

clan_url = stats_royale_url + CLAN
r = requests.get(clan_url)
html_doc = r.text

'''
Saving this legacy code for future testing
with open("test_html.html", encoding="utf8") as f:
    html_doc = f.read()
'''

data_load = createDataFile(html_doc)
