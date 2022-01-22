from celery.utils.log import get_task_logger
from djangoWebsite.celery import app
from .updateScript_gym import main
from celery.contrib import rdb
import os
import sys
logger = get_task_logger(__name__)
from django.conf import settings
random_dogs = os.listdir(settings.MEDIA_ROOT)


@app.task()
def gym_reg_task(gym, url, uid):
    logger.info(f'Start tracking {gym}')
    # using telnet to debug celery
    #rdb.set_trace()
    TOKEN = os.getenv('DISCORD_TOKEN')
    sys.exit(main(gym, url,TOKEN, uid))
    