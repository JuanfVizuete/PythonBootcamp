import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get the API KEY in the website - https://www.alphavantage.co/documentation/
API_KEY_STOCK = os.environ.get("API_KEY_STOCK")
API_KEY_NEWS = os.environ.get("API_KEY_NEWS")

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two
# prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK,
}

response_stock = requests.get(STOCK_ENDPOINT, params=parameters_stock)
data_stock = response_stock.json()
print(data_stock)
data_stock_days = data_stock["Time Series (Daily)"]
data_list = [value for (key, value) in data_stock_days.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#print(yesterday_closing_price)
#print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
#print(diff_percent)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

if abs(diff_percent) > 5:
    parameters_news = {
        "apiKey": API_KEY_NEWS,
        "qInTitle": COMPANY_NAME,
    }
    response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    articles = response_news.json()
    three_articles = articles[:3]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

formatted_articles_list = [f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

client = Client(account_sid, auth_token)
for article in formatted_articles_list:
    message = client.messages.create(
        body=article,
        from_="+16183894198",   #Twilio number
        to="+593992626854",    #Verified numbers in Twilio - destinatario
    )
    print(message.status)



