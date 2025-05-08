import requests
import os
import datetime as dt
from dotenv import load_dotenv
from pprint import pprint
from newsapi import NewsApiClient
from twilio.rest import Client

load_dotenv("Day36_StockTradingNewsAlert/.env")

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
ALPHA_VINTAGE_URL = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = dt.date.today()
YESTERDAY = TODAY - dt.timedelta(days=1)
DAY_BEFORE_YESTERDAY = TODAY - dt.timedelta(days=2)
# print(YESTERDAY, DAY_BEFORE_YESTERDAY)

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_KEY
}
response = requests.get(url=ALPHA_VINTAGE_URL, params=alpha_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
day_before_yesterday_data = data[str(DAY_BEFORE_YESTERDAY)]
yesterday_data = data[str(YESTERDAY)]


def rule_of_three(yesterday_data: dict, day_before_yesterday_data: dict) -> bool:
    day_before_yesterday_close = float(day_before_yesterday_data["4. close"])
    yesterday_close = float(yesterday_data["4. close"])
    increase_percentage = yesterday_close/day_before_yesterday_close
    # print(yesterday_close, day_before_yesterday_close)
    if increase_percentage > 1.05:
        print("Get News")
        return True, (increase_percentage*100)-100
    else:
        return False, None


increased_more_than_five_percent, percentage = rule_of_three(
    yesterday_data=yesterday_data, day_before_yesterday_data=day_before_yesterday_data)

# print(increased_more_than_five_percent)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if increased_more_than_five_percent:
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    # top_headlines = newsapi.get_top_headlines(q=STOCK, page_size=10)
    all_articles = newsapi.get_everything(q=STOCK, page_size=3)["articles"]
    articles_title_and_description = [
        f"Headline: {i['title']}.\nBrief: {i['description']}" for i in all_articles if all_articles]
    # pprint(articles_title_and_description)

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    message_body = "\n".join(articles_title_and_description)
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"""TSLA: 🔺{percentage}%
            {message_body}""",
        from_="+16066442593",
        to="+525521868386",
    )
    print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
