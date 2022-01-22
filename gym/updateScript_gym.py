"""Monitors the given course and send update when a spot frees up

    Usage: change the url to the course, chagne the word looking for to however, many people is registered in the class
    , subscribe to the printed website to recieve notification
"""

import time
import smtplib
import discord
import datetime
import gc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random


def main(gym, url, TOKEN, uid):
    print(url)
    gym = str(gym)
    url = str(url)
    uid = int(uid)
    print(f"Start Traking {gym}")
    
    def send_discord_message(word):
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)
        @client.event
        async def on_ready():
            await client.get_user(uid).send(f'Register for {gym} here {url} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {gym} here {url} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {gym} here {url} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {gym} here {url} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {gym} here {url} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {gym} here {url} RIGHT NOW!!!!!!!!!!!')
            await client.close()
        
        client.run(TOKEN)


        
    def get_css_element(driver):
        driver.get(url)
        return driver.find_element(By.CSS_SELECTOR, ".spots > span").text.lower()
    
    
    def update_loop():
    ## Keeps looping through the website until a spot is open
        options =  webdriver.FirefoxOptions()
        #options.binary_location = "/usr/bin/chromedriver"
        options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("--enable-javascript")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
        with webdriver.Firefox(options=options) as driver:
            print("did i even get here")
            try:
                status = get_css_element(driver)
                print(status)
                while True:
                    try:
                        assert status == "full"
                        time.sleep(random.randint(10,20)) 
                    except AssertionError: 
                        try:
                            send_discord_message(gym)
                            print("discord done")
                        except:
                            print("something went wrong with discord sending stuff")
                        break
                    except:
                        time.sleep(random.randint(10,20)) 
                        continue
            except:
                send_discord_message(f'Something went wrong with the tracker for gym. Please let Wilson know')
                
    update_loop()

# if __name__ == "__main__":
#     course = input("course")
#     noti_email = input("email")
#     url = input('url')
#     registered = input('250')
#     main(course, noti_email, url, registered)




