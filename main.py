import requests
from twilio.rest import Client
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."

api_key_stock = [YOUR KEY]
rest_api_stock = "https://www.alphavantage.co/query"
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock,
}

response_stock = requests.get(url=rest_api_stock, params=parameters_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()

list_stock = data_stock["Time Series (Daily)"].items()
fluctuation = float(list(list(list_stock))[0][1]["4. close"]) - float(list(list(list_stock))[1][1]["4. close"])

date_yesterday = list(list(list_stock))[0][0]
percentage_change = float((fluctuation / float(list(list(list_stock))[1][1]["4. close"]))*100)
if percentage_change > 0:
    change_message = f"↑{percentage_change}%"
elif percentage_change < 0:
    change_message = f"↓{percentage_change}%"
else:
    change_message = f"{percentage_change}%"


api_key_news = [YOUR KEY]
rest_api_news = "https://newsapi.org/v2/everything"
parameters_news = {
    "q" : f"{COMPANY_NAME}",
    "from" : date_yesterday,
    "sortBy" : "popularity",
    "apiKey" : api_key_news
}

response_news = requests.get(url=rest_api_news, params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()

new_heading_1 = data_news["articles"][0]["title"]
new_heading_2 = data_news["articles"][1]["title"]
new_heading_3 = data_news["articles"][2]["title"]

news_brief_1 = html.unescape(data_news["articles"][0]["description"])
news_brief_2 = html.unescape(data_news["articles"][1]["description"])
news_brief_3 = html.unescape(data_news["articles"][2]["description"])

account_sid = [YOUR-ACCOUNT-SID]
auth_token = [YOUR-AUTH-TOKEN]

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f"{STOCK}: {change_message}\n\nHeadline: {new_heading_1}\n\nBrief: {news_brief_1}",
    from_=[virtual-number-by-twilio],
    to=[your-number],
)

message_2 = client.messages \
    .create(
    body=f"{STOCK}: {change_message}\n\nHeadline: {new_heading_2}\n\nBrief: {news_brief_2}",
    from_=[virtual-number-by-twilio],
    to=[your-number],
)

message_3 = client.messages \
    .create(
    body=f"{STOCK}: {change_message}\n\nHeadline: {new_heading_3}\n\nBrief: {news_brief_3}",
    from_=[virtual-number-by-twilio],
    to=[your-number],
)




"""
SAMPLE OUTPUT IN SMS : 

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

