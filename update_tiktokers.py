from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
import gspread

data = {}
authorname = []
nickname = []
follower = []
view = []
like = []
comment = []
share = []
engagement_rate = []
engagement_rate_by_reach = []

# Use my credentials
sa = gspread.service_account(filename = "/Users/tony/Downloads/skilful-rig-361105-0ee73c40b317.json")

# Enter the sheet's name
user_input_spreadsheet = input("Enter the name of the Spreadsheet: ")
sh = sa.open(user_input_spreadsheet)
user_input_worksheet = input("Enter the name of the Worksheet: ")
worksheet = sh.worksheet(user_input_worksheet)

# Get all urls from the first column
urls_list = worksheet.col_values(1)

# Loop thru urls
for url in urls_list:
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    time.sleep(1)
    browser.close()

    soup = BeautifulSoup(html, "html.parser")

    data = json.loads(soup.find("script", type="application/json").string)

    sum_playcount = 0
    count = 0
    engagementcount = 0
    sum_engagmentcount = 0

    itemmodule = data["ItemModule"]
    for item in itemmodule.values():

        # Get the author name
        tiktoker_name = item["author"]

        # Get the nickname
        tiktoker_nickname = item["nickname"]

        # Get the number of followers
        authorstats = item["authorStats"]
        followercount = authorstats["followerCount"]

        # Get the number of views
        stats = item["stats"]
        playcount = stats["playCount"]
        sum_playcount += playcount

        # Get the number of engagement
        diggcount = stats["diggCount"]
        commentcount = stats["commentCount"]
        sharecount = stats["shareCount"]
        engagementcount = diggcount + commentcount + sharecount
        sum_engagmentcount += engagementcount

        count += 1

    # Calcute avg.views and ER
    avg_view = round(sum_playcount / count)
    avg_engagment = round(sum_engagmentcount / count)
    engagement = round(((avg_engagment / followercount) * 100), 2)
    engagement_by_reach = round(((avg_engagment / avg_view) * 100), 2)

    # Add data to the list
    authorname.append(tiktoker_name)
    nickname.append(tiktoker_nickname)
    follower.append(followercount)
    view.append(avg_view)
    engagement_rate.append(engagement)
    engagement_rate_by_reach.append(engagement_by_reach)

# Put data in a dict
data = {
"TikToker": authorname,
"Nickname": nickname,
"Followers": follower,
"Avg.Views": view,
"ER %": engagement_rate,
"ER by Reach %": engagement_rate_by_reach
}

df = pd.DataFrame(data)

# Use Thousand separator (*But this seems to change its type from int to str?)
df["Followers"] = df["Followers"].apply('{:,}'.format)
df["Avg.Views"] = df["Avg.Views"].apply('{:,}'.format)

# Update the worksheet
worksheet_result = sh.add_worksheet(title="result", rows=100, cols=20)
worksheet_result.update([df.columns.values.tolist()] + df.values.tolist())
