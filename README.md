# TikTok Scraper in Python with Selenium and Google Sheets Api
This is an unofficial tool for collecting TikTokers' metadata.

## Background
👋 Hi, My name is Tony Yu, I'm working as a growth manager at a social media company. I work with a lot of influencers for growing apps, and it had been a pain in the ass collecting each video's views, likes, comments, shares, etc., and then writing them down in a spreadsheet over and over again. So I made this scraper to fetch the info I need, and I wanted to share it with people who may happen to be interested in it.

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

Here’s how to get one:
1. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”. Fill out the form. Click “Create” and “Done”.
2. Press “Manage service accounts” above Service Accounts.
3. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
4. Select JSON key type and press “Create”. You will automatically download a JSON file with credentials.
5. Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account.

Remember to substitute the file directory for the credentials json file with yours.

<!---
yushengnan0525/yushengnan0525 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
