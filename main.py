
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)





driver = webdriver.Chrome(options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")
time.sleep(5)



# #target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# #enter username and password
username.clear()
username.send_keys("your_email_here")  # Replace with your actual email
time.sleep(4)
password.clear()
password.send_keys("your_password_here")  # Replace with your actual password
time.sleep(4)


# #target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(30)

# #We are logged in!


# Pehle search results ka link open
driver.get("https://www.facebook.com/search/posts/?q=i%20need%20website")

# Wait until cards appear
WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "xdj266r") and contains(@class, "x14z9mp")]'))
)


for _ in range(30):  # 10 baar scroll karein, aap is number ko badha ya ghatta sakte ho
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) 

# Store data here
data = []

# cards scrape
cards = driver.find_elements(
    By.XPATH,
    '//div[contains(@class, "xdj266r") and contains(@class, "x14z9mp")]'
)

for index, card in enumerate(cards, start=1):
    try:
        name_elem = card.find_element(By.XPATH, ".//h2//span")
        name = name_elem.text.strip()

        text_elem = card.find_element(By.XPATH, ".//div[@dir='auto']")
        post_text = text_elem.text.strip()

        print(f"Post #{index}")
        print("Name:", name)
        print("Text:", post_text)
        print("-" * 50)
        data.append({"Name": name, "Text": post_text})

    except:
        pass

    

import pandas as pd

df = pd.DataFrame(data)
df.to_excel("facebook_posts.xlsx", index=False)

print(f"Saved {len(data)} posts to facebook_posts.csv")
