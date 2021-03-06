from celery.utils.log import get_task_logger
from djangoWebsite.celery import app
from .updateScript import main
from celery.contrib import rdb
import os
import sys
logger = get_task_logger(__name__)
from django.conf import settings
random_dogs = os.listdir(settings.MEDIA_ROOT)


@app.task()
def course_reg_task(course, email, url, number, uid):
    logger.info(f'Start tracking {course}')
    # using telnet to debug celery
    #rdb.set_trace()
    username = os.getenv("username1")
    password = os.getenv("password")
    TOKEN = os.getenv('DISCORD_TOKEN')
    sys.exit(main(course, email, url, number, username, password, TOKEN, uid))
    