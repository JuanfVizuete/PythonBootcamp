from itertools import product

import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

#URL_AMAZON = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PWD")


def send_email(to_email, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        # Securing connection
        connection.starttls()
        # Login
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # Send mail
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}".encode("utf-8")
        )

def getAmazonProductInfo(url, info):

    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US",
        "Priority": "u=0, i",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    }
    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())

    if info == "price":
        price = soup.select_one(selector="div span span[aria-hidden='true']").text
        price_float = float(price.split("$")[1].replace(",",""))
        print(price_float)
        return price_float
    else:
        item = soup.select_one(selector="h1 span[id='productTitle']").getText()
        item = item.replace('\n', ' ').replace('\r', '')
        product_title = " ".join(item.split())
        print(product_title)
        return product_title


products = {
    0: {
        'name': getAmazonProductInfo("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", "name"),
        'price': getAmazonProductInfo("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", "price"),
        'url': 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1',
        'buy_price': 100,    # Here you enter the desired buy price
    },
    1: {
        'name': getAmazonProductInfo("https://www.amazon.com/dp/B0C7JYX6LN?ref=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&ref_=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&social_share=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&th=1", "name"),
        'price': getAmazonProductInfo("https://www.amazon.com/dp/B0C7JYX6LN?ref=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&ref_=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&social_share=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&th=1", "price"),
        'url': 'https://www.amazon.com/dp/B0C7JYX6LN?ref=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&ref_=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&social_share=cm_sw_r_cp_ud_dp_8STWF53FSGR5489ZKKHH&th=1',
        'buy_price': 1800,   # Here you enter the desired buy price
    }
}

for key, value in products.items():
    print(value['name'])
    print(value['price'])
    print(type(value['buy_price']))
    if value['price'] < value['buy_price']:
        send_email("juanvizuete.python@yahoo.com", "Amazon Price Alert!",
                    f"{value['name']} is now ${value['price']} ! \nCheck it out: {value['url']}")

