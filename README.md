# TikTok Scraper in Python with Selenium and Google Sheets Api
This is an unofficial tool for collecting TikTokers' metadata.

## Background
👋 Hi, My name is Tony Yu, I'm working as a growth manager at a social media company. I collab with a lot of influencers for work, and it had been a pain in the ass collecting each video's views, likes, comments, shares, etc., and then writing them down in a spreadsheet over and over again. So I made this scraper to fetch the info I need, and I wanted to share it with people who may happen to be interested in it.

## Getting Started
To start use the scrapper follow the instruction below.

### Selenium
We're gonna use Selenium and Chrome Webdriver to auto open a web browser and visit TikTok.
```sh
- pip install selenium
```
Download Chrome Webdriver (https://chromedriver.chromium.org/downloads), put the webdriver in /usr/local/bin

### gspread and Google Sheets API
```sh
- pip install gspread
```
To access spreadsheets via Google Sheets API you need to authenticate and authorize your application.


#### Enable API Access for a Project
Head to Google Developers Console (https://console.developers.google.com/) and create a new project.
In the box labeled “Search for APIs and Services”, search for “Google Drive API” and “Google Sheets API” and enable them.


#### Using Service Account
A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs.

Instruction -> https://docs.gspread.org/en/latest/oauth2.html
YouTube Guide -> https://www.youtube.com/watch?v=bu5wXjz2KvU

Remember to substitute the credentials file directory with yours in the script (update_tiktokers.py).

## Use the scrapper
Run the script in Terminal, enter the spreadsheet name and the worksheet name.

## Result Example
![image](https://user-images.githubusercontent.com/49832190/188074532-1ffa3149-8fc3-444d-985e-8e1ff34bdec0.png)


<!---
yushengnan0525/yushengnan0525 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
