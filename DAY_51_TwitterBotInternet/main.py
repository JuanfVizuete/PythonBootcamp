from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = os.getenv('PROMISED_DOWN')
PROMISED_UP = os.getenv('PROMISED_UP')
TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        start_test = self.driver.find_element(By.CSS_SELECTOR,
                                              'a[aria-label="start speed test - connection type multi"]')
        start_test.click()
        time.sleep(65)

        download = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        upload = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        self.down = float(download.text)
        self.up = float(upload.text)
        print(self.down, self.up)

    def tweet_at_provider(self):
        time.sleep(2)
        self.driver.get('https://x.com/home')
        sign_in_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
        sign_in_btn.click()
        time.sleep(3)
        email_box = self.driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
        email_box.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(2)
        username_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_box.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(2)
        pwd_box = self.driver.find_element(By.NAME, 'password')
        pwd_box.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(6)
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Post text"]')
        tweet_box.send_keys(f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up Mbps "
                            f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up Mbps")
        time.sleep(1)
        post_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"')
        post_btn.click()
        time.sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < float(PROMISED_DOWN) or bot.up < float(PROMISED_UP):
    bot.tweet_at_provider()


