from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def buyStoreItem(store):
    # Checking the store items for prices and buy the most expensive
    for item in reversed(store):
        item_price = int(item.text.split('\n')[0].split(' - ')[1].replace(',', ''))
        #print(item_price)
        money = int(driver.find_element(By.CSS_SELECTOR, '#money').text.replace(',', ''))
        #print(money)
        if money >= item_price:
            item.click()
            break

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

timecheck = time.time() + 5
is_game_over = False
time_over = time.time() + (60*5)

while not is_game_over:
    cookie.click()
    if time.time() > timecheck:
        # Obtain only available items in the store
        store = driver.find_elements(By.CSS_SELECTOR, '#store div[class=""]')
        buyStoreItem(store)

        #Restart clicking cookie time
        timecheck = time.time() + 5
    if time.time() > time_over:
        is_game_over = True
        cookies_p_second = driver.find_element(By.CSS_SELECTOR, '#cps').text
        print(f"My cookies/second achieved are: {cookies_p_second}")




