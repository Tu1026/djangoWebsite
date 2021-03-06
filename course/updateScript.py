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


def main(course, noti_email, url, seatType, username, password, TOKEN, uid):
    print(username)
    print(url)
    course = str(course)
    noti_email = str(noti_email)
    url = str(url)
    seatType = str(seatType)
    uid = int(uid)
    print(noti_email)
    print(seatType)
    print(f"Start Traking {course}")
        
    def process_seat_type():
        if seatType == "general":
            return "tr:nth-child(3) strong", "tr:nth-child(3) strong"
        elif seatType == "restricted":
            return "tr:nth-child(4) strong", "tr:nth-child(4) strong"
        else:
            return "tr:nth-child(3) strong", "tr:nth-child(4) strong"
        
    general_selector, restricted_selector, = process_seat_type()
    
    def send_discord_message(word):
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)
        @client.event
        async def on_ready():
            await client.get_user(uid).send(f'Register for {word} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {word} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {word} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {word} RIGHT NOW!!!!!!!!!!!')
            await client.get_user(uid).send(f'Register for {word} RIGHT NOW!!!!!!!!!!!')
            await client.close()
        

        client.run(TOKEN)


    #Reference from https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
    def send_email(username, password):
        """send email to the person who wishes to recieve notification
        """
        sent_from = username
        to = [noti_email]
        subject = 'Course registeration for ' + course
        body = 'The course you want has a seat open!!'
        message ='Subject: {}\n\n{}'.format(subject, body)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(username, password)
        server.sendmail(sent_from, to, message)
        server.close()
        
    def maintnence_time():
        t = datetime.datetime.today()
        return t.hour >= 2 and t.hour <= 5
    
    def sleep_if_maintnence():
        if maintnence_time():
            curr_time = datetime.datetime.today()
            new_time = curr_time.replace(hour=5, minute=30)
            time.sleep((new_time - curr_time).total_seconds())
            print(f'sleeping right now till 4.20 AM for {(new_time - curr_time).total_seconds()} seconds to avoid scheduled maintenence')
            t = datetime.datetime.today()
            print(f'waking up at time {t}') 

        
    def get_css_element(driver):
        driver.get(url)
        return driver.find_element(By.CSS_SELECTOR, general_selector).text, driver.find_element(By.CSS_SELECTOR, restricted_selector).text
    
    def check_seat_status(general, restricted, driver):
        try:
            driver.get(url)
            general_new, restreicted_new = get_css_element(driver)
            assert general_new == general
            assert restreicted_new == restricted
            return general_new, restreicted_new
        except AssertionError:
            raise AssertionError
        except:
            raise
        
    
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
        restricted = 0
        general = 0
        with webdriver.Firefox(options=options) as driver:
            try:
                general, restricted = get_css_element(driver)
                while True:
                    try:
                        sleep_if_maintnence()
                        print(f"still no seats available for {course}")
                        general, restricted = check_seat_status(general, restricted, driver)
                        gc.collect()
                        print("sleeping to avoid bot detection")
                        time.sleep(random.randint(20,40)) 
                    except AssertionError: 
                        try:
                            send_discord_message(course)
                            print("discord done")
                            send_email(username, password)
                            print("email notificaiton sent")
                        except:
                            print("something went wrong with emailing stuff or FB stuff")
                        break
                    except:
                        time.sleep(random.randint(20,40)) 
                        continue
            except:
                send_discord_message(f'Something went wrong with {course}')
                
    sleep_if_maintnence()
    update_loop()

# if __name__ == "__main__":
#     course = input("course")
#     noti_email = input("email")
#     url = input('url')
#     registered = input('250')
#     main(course, noti_email, url, registered)




