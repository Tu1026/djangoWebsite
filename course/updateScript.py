"""Monitors the given course and send update when a spot frees up

    Usage: change the url to the course, chagne the word looking for to however, many people is registered in the class
    , subscribe to the printed website to recieve notification
"""

from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
import smtplib
import os
import discord
import datetime
import gc

def main(course, noti_email, url, registered, username, password, TOKEN, uid):
    course = str(course)
    noti_email = str(noti_email)
    url = str(url)
    registered = str(registered)
    print("at least it's a start ")
    def send_discord_message(word):
        client = discord.Client()
        @client.event
        async def on_ready():
            await client.get_channel(uid).send(f'Register for {word}RIGHT NOW!!!!!!!!!!!')
            await client.get_channel(uid).send(f'Register for {word}RIGHT NOW!!!!!!!!!!!')
            await client.get_channel(uid).send(f'Register for {word}RIGHT NOW!!!!!!!!!!!')
            await client.get_channel(uid).send(f'Register for {word}RIGHT NOW!!!!!!!!!!!')
            await client.get_channel(uid).send(f'Register for {word}RIGHT NOW!!!!!!!!!!!')
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

    def update_loop():
    ## Keeps looping through the website until a spot is open
        while True:
            try: 
                text = soup.get_text()
                text_list = text.split()
                word_looking_for = "Registered:" + registered
                t = datetime.datetime.today()
                # if the amount of people registered has not changed keep looping
            except:
                time.sleep(10) 
                continue
            
            if word_looking_for in text_list:
                # wait 10 seconds,
                print(f"No seats avaliable yet updating in 10 seconds. Current time: {t.month}/{t.day} {t.hour}:{t.minute}:{t.second}")
                time.sleep(10)
                if t.hour >= 2 and t.hour <= 4:
                    time_sleep = datetime.timedelta(hours=2, minutes=20)
                    print(f'sleeping right now till 4.20 AM for{time_sleep.total_seconds()} seconds to avoid scheduled maintenence')
                    time.sleep(time_sleep.total_seconds())
                    t = datetime.datetime.today()
                    print(f'waking up at time {t}') 
                # continue with the script,
                del text, text_list, word_looking_for, t
                gc.collect()
                continue
                
            # if the amout of people registered has changed do a pop up and send a notificaiton on the website
            else:
                # notify.send("register for " + course + " NOW")
                try:
                    # log into server account to send message
                    # config = ConfigParser()
                    # config.read('config.ini')
                    # username = config.get("email", "username")
                    # password = config.get("email", "password")
                    # send_fb_message("register for " + course + "NOWWWWWWW")
                    send_discord_message(course)
                    send_email(username, password)
                    print("email notificaiton sent")
                except:
                    print("something went wrong with emailing stuff or FB stuff")
                break

    #get information from user
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    update_loop()

# if __name__ == "__main__":
#     course = input("course")
#     noti_email = input("email")
#     url = input('url')
#     registered = input('250')
#     main(course, noti_email, url, registered)




