from bs4 import BeautifulSoup

def createDataFile(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")

    data = soup.find_all("div", class_="clan__rowContainer")

    # Each member of the clan will have a seperate dictionary within the members dictionary
    clan_data = {}

    # Define keys for each individual member's dictionary
    keys = ["Rank", "Name", "Level", "League", "Trophies", "Crowns", "Donations", "Role"]
    i = 0

    for d in data:
        # Each member of the clan has a row in the html table, defined by the class clan__row
        member_data = d.find_all("div", class_="clan__row")

        # Each member's unique user ID is housed in a link. Skip the first 31 characters: http://statsroyale.com/profile/
        user_id = d.a["href"][31:]
        clan_data[user_id] = {}
        for col in member_data:
            clan_data[user_id][keys[i]] = col.get_text().strip()
            i = i + 1
        i = 0
    return clan_data

